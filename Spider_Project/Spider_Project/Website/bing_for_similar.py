import json
import requests
import sqlite3
import traceback
from bs4 import BeautifulSoup


HEAD = {
		"content-type": "multipart/form-data; boundary=----WebKitFormBoundaryhvLAoToX3FQzOR8A",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
		"cookie": "MMCA=ID=392CCB34EBCB4C258A10DC67E11EBF6C; _IDET=VSNoti2=20191230&MIExp=0&InsSte=11&HSNoti2=20191231; ipv6=hit=1582788861882&t=4; MUID=062A4CE6DDF8600721EA4166DC5361B8; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=BF64F4591F764B1C8F5B6F75B67AD449&dmnchg=1; MUIDB=062A4CE6DDF8600721EA4166DC5361B8; fbar=imgfbar=1; _EDGE_S=mkt=zh-cn&SID=0C1F8F53CD3A6FAD2EE58129CC146EA9; _FP=hta=on; imgv=lts=20200224&lodlg=1&gts=20200116; BPF=X=1; ipv6=hit=1582773085952&t=4; _SS=SID=0C1F8F53CD3A6FAD2EE58129CC146EA9&bIm=926271&h5comp=0; ULC=P=58C0|17:9&H=58C0|17:9&T=58C0|17:9; ENSEARCH=BENVER=0; SRCHUSR=DOB=20190816&T=1582785195000; SRCHHPGUSR=CW=1903&CH=920&DPR=1&UTC=480&WTS=63718381995&HV=1582852533",
	}


def connect_to_sql(key):
	conn = sqlite3.connect("Bing_for_Similar.db")
	creat_table = """
	create table if not exists {}(
		imageId primary key ,
		contentUrl,
		imageInsightsToken)
	""".format(key)
	cur = conn.cursor()
	cur.execute(creat_table)
	conn.commit()
	return conn, cur


def get_search_imgs(keyword, startnum):
	original_url = """
		https://www.bing.com/images/async?q={key}&first={first}&count=35&relp=35
	""".format(key=keyword, first=startnum)

	res2 = requests.get(original_url, headers=HEAD, timeout=(6, 10))
	soup = BeautifulSoup(res2.text, 'lxml')
	try:
		url_josn = soup.select("a.iusc")
		searchurls = [json.loads(m.get("m"))["murl"] for m in url_josn]
		return searchurls
	except:
		print(traceback.print_exc())
		return "url requests failed "


def oneset_urls(restext):
	res_json = json.loads(restext)
	maxnum = res_json["totalEstimatedMatches"]
	values = res_json["value"]
	urls_lists = [
		[value["imageId"], value["contentUrl"], value["imageInsightsToken"]]
		for value in values
	]
	return urls_lists, maxnum


def new_search_imgs(keyword):
	first_url = """
		https://www.bing.com/images/api/custom/search?q={key}&count=35&offset=0&skey=ckMBckKPZI2srnsjmYafRRrf-3ypo1A2muAT-Du8Zgw&safeSearch=Strict&IG=A224B4CF1E1C474A86890208102883E7&IID=idpfs&SFX=3&mkt=zh-CN&ensearch=1&FORM=BESBTB
	""".format(key=keyword)
	#first_url = "https://www.bing.com/images/api/custom/search?q=surgical%20mask&count=35&offset=0&skey=ckMBckKPZI2srnsjmYafRRrf-3ypo1A2muAT-Du8Zgw&safeSearch=Strict&IG=A224B4CF1E1C474A86890208102883E7&IID=idpfs&SFX=3&mkt=zh-CN&ensearch=1&FORM=BESBTB"
	s_res = requests.get(first_url, headers=HEAD, timeout=(10, 10))

	# 生成第一个url列表
	totalurl, maxnum = oneset_urls(s_res.text)

	for i in range(35, maxnum, 35):
		search_url = """
		https://www.bing.com/images/api/custom/search?q={key}&count=50&offset={offset}
		&skey=ckMBckKPZI2srnsjmYafRRrf-3ypo1A2muAT-Du8Zgw&safeSearch=Strict&IG=A224B4CF1E1C474A86890208102883E7&IID=idpfs&SFX=3
		""".format(key=keyword, offset=i)
		offset_res = requests.get(search_url, headers=HEAD, timeout=(6, 10))
		totalurl.extend(oneset_urls(offset_res.text)[0])

	return totalurl


def get_similar_json(bench_url, start_num, imgtoken, keyword):
	imgjson = json.loads("""
		{
		"imageInfo": {
			"source": "BingImageIndex"
		},
		"knowledgeRequest": {
			"invokedSkills": ["SimilarImages"],
			"count": 35
		}
	}
	""")
	imgjson["imageInfo"]["url"] = bench_url
	imgjson["knowledgeRequest"]["offset"] = start_num
	imgjson["imageInfo"]["imageInsightsToken"] = imgtoken

	bodys = """------WebKitFormBoundaryhvLAoToX3FQzOR8A
Content-Disposition: form-data; name="knowledgeRequest"

{img_info}
------WebKitFormBoundaryhvLAoToX3FQzOR8A--
""".format(img_info=json.dumps(imgjson))

	similarurl = "https://www.bing.com/images/api/custom/knowledge?q={key}&skey=ckMBckKPZI2srnsjmYafRRrf-3ypo1A2muAT-Du8Zgw&safeSearch=Strict&IG=45C3C407EA154740BC03ECC591896682&IID=idpins&SFX=2".format(key=keyword)

	res = requests.post(similarurl, data=bodys, headers=HEAD)
	try:
		similar_json = json.loads(res.text)
		return similar_json
	except json.decoder.JSONDecodeError:
		print("request similar url failed")
		return res.text


def get_similar_url(similar_json):
	try:
		data = similar_json["tags"][0]["actions"][0]["data"]
	except:
		return -1, -1
	maxnum = data["totalEstimatedMatches"]
	values = data["value"]
	urls_lists = [
		[value["imageId"], value["contentUrl"], value["imageInsightsToken"]]
		for value in values
	]
	return urls_lists, maxnum


def insert_to_sq(cur, conn, values, key):
	# indexkey = "imageId, contentUrl, imageInsightsToken"
	ins_cmd = """replace into {a} (imageId, contentUrl, imageInsightsToken) values (?, ?, ?)
	""".format(a=key)  #  on duplicate key update 	contentUrl=values(contentUrl), imageInsightsToken=values(imageInsightsToken)
	cur.executemany(ins_cmd, values)
	conn.commit()
	return "Insert Success"
	# print(1)

	# with open(key + "ur.csv", 'a+', newline='') as csvfile:
	# 	writers = csv.writer(csvfile)
	# 	for value in values:
	# 		writers.writerow(value)


def deal_similar_url(bench_url, imgtoken, keyword):
	oneset_json = get_similar_json(bench_url, 1, imgtoken, keyword)
	if not isinstance(oneset_json, dict):
		print("erro")
		return oneset_json
	totalurls, maxnum = get_similar_url(oneset_json)
	if maxnum == -1:
		return -1
	for i in range(35, maxnum, 35):
		temp_similars = get_similar_json(bench_url, i, imgtoken, keyword)
		urs = get_similar_url(temp_similars)
		try:
			totalurls.extend(urs[0])
		except:
			continue
	print(len(totalurls))
	return totalurls


if __name__ == '__main__':

	for keyword in ["高清大头照", "证件照", "大头照 男"]:
		conn, cur = connect_to_sql(keyword.replace(" ", "_"))

	# keyword = "番茄盆栽"
		res = new_search_imgs(keyword)

		for idx, res_i in enumerate(res):
			if idx == 200:
				break
			print(str(idx))
			total_urls = deal_similar_url(res_i[1], res_i[2], keyword)
			try:
				status = insert_to_sq(cur, conn, total_urls, keyword.replace(" ", "_"))
				print(status)
			except:
				continue
		conn.close()

