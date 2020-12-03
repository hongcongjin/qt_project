import requests
from bs4 import BeautifulSoup
import json
import sqlite3


HEAD = {}
simiHead = {}
# HEAD["cookie"] = "CGIC=Inx0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; SEARCH_SAMESITE=CgQIs44B; ANID=AHWqTUlfKrIRsTCHFppd01Q1KBTvFkjB8gUvV1SbVpiW7rVvaf00WId_NH-Xcpf1; OTZ=5257596_24_24__24_; NID=195=gKpx8V4ZqvSJIPPNZme6yj67dNsOBbdvZGBBXo81eEJiYplX3qO71As-7sze6QQbVWQ0MGGca1Dvpa4QfzSCxIHQNksmZNMce0vvhle0e39aaPmwrT-VWy5Iv2wZjZ12pA34BauCQw82Uzn16zeDiHOIoxjry8WQB9-YRJOnLeae7i9NnJFU1G77EYrHMRdkVQETFgnHOpRG638hq8NrAp5GiLN40q2o9EMsYmw; 1P_JAR=2020-01-08-09"
HEAD["cookie"] = "SEARCH_SAMESITE=CgQIs44B; ANID=AHWqTUlfKrIRsTCHFppd01Q1KBTvFkjB8gUvV1SbVpiW7rVvaf00WId_NH-Xcpf1; OTZ=5257596_24_24__24_; NID=195=fkJf2uRC-WhODFdaaU_7ITmCIanS0sRpW7HD15SJeXqqhDh1eIh0cdRAAkDss-ljybucaOAdBh438Fbx5QsKgvJRSc3n-I6bGWuDN4iRzlt3MPLjpDPSuyrmFZHld3v_7ZB1jsGxSl15dd6P70m4MwZHvR21lKGlqXW7xgD3MusPu9qXEWM8RLbSm_Az9_rbZG5tk99Ppxo1HtPCkEhLaIrd9QCRhSJzzCivkH0; 1P_JAR=2020-01-09-03"
simiHead["cookie"] = "CGIC=EhQxQzFHSVdBX2VuVFc4NzdUVzg3NyJ8dGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOQ; SEARCH_SAMESITE=CgQIs44B; ANID=AHWqTUlfKrIRsTCHFppd01Q1KBTvFkjB8gUvV1SbVpiW7rVvaf00WId_NH-Xcpf1; OGPC=19016257-10:; OGP=-19016257:; SID=uweIeszJX2V6WO-18v1UYQ04YBWB9jqDxfQdcePeo5mPrbpXV5OPW5lK0FMmeDDyUt9SRQ.; __Secure-3PSID=uweIeszJX2V6WO-18v1UYQ04YBWB9jqDxfQdcePeo5mPrbpXM7SdoTMyNXWUsy6uI4BCsQ.; HSID=AfcSarWp9QNsOTjG_; SSID=AwFbosiHCi28dX-1-; APISID=tUCz5LBeA_YQMn61/Ahqp62sD9yPVZXuyT; SAPISID=7HrPAwGTMBdcrD9X/AebYDFfFwU_7Q18At; __Secure-HSID=AfcSarWp9QNsOTjG_; __Secure-SSID=AwFbosiHCi28dX-1-; __Secure-APISID=tUCz5LBeA_YQMn61/Ahqp62sD9yPVZXuyT; __Secure-3PAPISID=7HrPAwGTMBdcrD9X/AebYDFfFwU_7Q18At; OTZ=5363120_24_24__24_; NID=201=03XfICHNIRHhrZ66EFlKG_chsxmKX-1R8wh3N-ofO4L7LVU_3NylL-QceIoU620dXOHU1O8HsAHubgPdkmlLK7GxkvorJDyb0rdu1gtWFjkkmupwDwghFQyteoEcqdowM6b3-BBdHJTMQJYp8hxBTEBnMJOfFMNuKYfbgLv9cjnM0ne6J_Dy4tDgINyxlAS-1PPBdIcuOUsXCQJy-nu5kk_nLBOOv-krnmbMo6J2Y5TzJSh4V1wtXekPV5UAUtmzwLxVwdMt2KttBuUJFv6X0_IE_kR_rxtMPqka1gaxbVOlbl8ufNj2ZflDNKaFZqF5AVZw1kiGmFECqoe8ee8oJVcDgzB8-9dyTDDzc9pCeytIK_aAzHJYKx2FuwU; 1P_JAR=2020-03-31-09; SIDCC=AJi4QfG-UZlzJmS9fWirQOPh5HCzAw9pbqHNcjPlzmhN56nr0tqu45TG6jadqmF8_ZtHxgntvQQ"
HEAD["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
simiHead["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"


def connect_to_sql(key):
    conn = sqlite3.connect("Google_for_Similar.db")
    creat_table = """
    create table if not exists {}(
        imageId primary key ,
        contentUrl,
        similarUrl)
    """.format(key)
    cur = conn.cursor()
    cur.execute(creat_table)
    conn.commit()
    return conn, cur


def similar_parse(eles):
    orurl = list()
    for ele in eles:
        try:
            el_js = json.loads(ele.text)
            oripic = el_js['ou']
            imgdii = "imgdii=" + el_js['id']
            docid = "docid=" + el_js['rid'] + '&'
            endpart = "&async=cidx:1,saved:0,iu:0,lp:0,_fmt:prog,_id:irc_imgrc1,_jsfs:Ffpdje"
            newsearch = "https://www.google.com/async/imgrc?" + docid + imgdii + endpart
            parturl = [imgdii, oripic, newsearch]
            orurl.append(parturl)
        except:
            continue
    return orurl


def original_parse(eles):
    orurl = list()
    for i in eles:
        try:
            url_js = i.attrs
            similar_search = url_js["href"]
            oripic = similar_search.split("imgurl=")[1].split("&")[0]
            docid = "docid=" + similar_search.split("docid=")[1].split("&")[0] + "&"
            imgdii = "imgdii=" + similar_search.split("tbnid=")[1].split("&")[0]
            endpart = "&async=cidx:1,saved:0,iu:0,lp:0,_fmt:prog,_id:irc_imgrc1,_jsfs:Ffpdje"
            newsearch = "https://www.google.com/async/imgrc?" + docid + imgdii + endpart
            parturl = [imgdii, oripic, newsearch]
            orurl.append(parturl)
        except:
            continue
    return orurl


def parse_method(soup, type):
    """
    :param soup:
    :param type: 1:original search, 2:similar search
    :return:
    """
    if type == 1:
        similarurl = soup.find_all("a", jsname="hSRGPd")  # hSRGPd
        orurl = original_parse(similarurl)
    else:
        similarurl = soup.find_all("div", class_="rg_meta notranslate")  # hSRGPd
        orurl = similar_parse(similarurl)

    return orurl


def searchurl(keyword, startnum):
    # search_url = "https://www.google.com/search?yv=3&tbm=isch&q={key}&ijn=1&start={num}&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc".format(key=keyword, num=startnum)
    search_url = "https://www.google.com/search?ei=nIsVXuX7ENuXr7wPhZCYiAg&rlz=1C1GIWA_enTW877TW877&yv=3&tbm=isch&q={key}&vet=10ahUKEwjluaWMxPPmAhXby4sBHQUIBoEQuT0IaigB.nIsVXuX7ENuXr7wPhZCYiAg.i&ved=0ahUKEwjluaWMxPPmAhXby4sBHQUIBoEQuT0IaigB&ijn=1&start={num}&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc".format(
        key=keyword, num=startnum)
    # newurl = "http://www.google.com/search?ei=UJsVXsGzCZO-wAO35KJg&yv=3&tbm=isch&q=girl&vet=10ahUKEwjBm4-J0_PmAhUTH3AKHTeyCAwQuT0IaigB.UJsVXsGzCZO-wAO35KJg.i&ved=0ahUKEwjBm4-J0_PmAhUTH3AKHTeyCAwQuT0IaigB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc"
    res = requests.get(search_url, timeout=(3, 10))
    soup = BeautifulSoup(res.text, "lxml")
    orurl = parse_method(soup, 1)
    return orurl


def get_all_search(keyword):
    total_url = []
    for i in range(0, 800, 100):
        one_hun = searchurl(keyword, i)
        total_url.extend(one_hun)
    return total_url


def similar_rimg(partsimilar):
    simi = requests.get(partsimilar, headers=HEAD, timeout=(3, 10))
    soup = BeautifulSoup(simi.text, "lxml")
    try:
        s = soup.select('a[href*="rimg"]')
        rimg = str(s[1].attrs["href"]).split("tbs=")[1].split("&")[0]
        return rimg
    except:
        return False


def search_simiar(keyword, start_num, rimg):
    """
    :param keyword:
    :param start_num:每次100
    :param rimg:
    :return: 返回格式[[ou, ru], [], [], []]
    """
    keypart = '&yv=3&q={key}&tbm=isch&vet=10ahUKEwj4_rLm5vXmAhVkJaYKHXtyASYQuT0IMCgB.b7wWXriLIOTKmAX75IWwAg.i&ved' \
              '=0ahUKEwj4_rLm5vXmAhVkJaYKHXtyASYQuT0IMCgB'.format(key=keyword)
    pagepart = '&ijn=2&start={num}&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc'.format(num=start_num)
    url = "https://www.google.com/search?ei=b7wWXriLIOTKmAX75IWwAg&tbs={rimg}".format(rimg=rimg) + keypart + pagepart
    ser = requests.get(url, headers=simiHead, timeout=(3, 10))
    soup = BeautifulSoup(ser.text, 'lxml')
    orurl = parse_method(soup, 2)
    return orurl


def get_one_similars(keyword, imgbyt):
    total_url = []
    # for i in range(0, 800, 100): ##  多页暂时无效
    one_hun = search_simiar(keyword, 0, imgbyt)
    total_url.extend(one_hun)
    return total_url


def insert_to_sq(cur, conn, values, key):
    # indexkey = "imageId, contentUrl, similarUrl"
    ins_cmd = """replace into {a} (imageId, contentUrl, similarUrl) values (?, ?, ?)
    """.format(a=key)  #  on duplicate key update 	contentUrl=values(contentUrl), imageInsightsToken=values(imageInsightsToken)
    cur.executemany(ins_cmd, values)
    conn.commit()
    return "Insert Success"


if __name__ == '__main__':
    for keyword in ["apple"]:
        conn, cur = connect_to_sql(keyword.replace(" ", "_"))
        total_ous = get_all_search(keyword)
        # with open('list.csv', 'w', encoding='utf-8', newline="") as f:
        #     wrte = csv.writer(f)
        #     wrte.writerows(total_ous)

        status = insert_to_sq(cur, conn, total_ous, keyword.replace(" ", "_"))

        for num, one in enumerate(total_ous):
            if num == 500:
                break
            print(str(num))
            rimg = similar_rimg(one[2])
            if not rimg:
                continue
            else:
                try:
                    all_similar = get_one_similars(keyword, rimg)
                    print("similar pic are  " + str(len(all_similar)))
                    status = insert_to_sq(cur, conn, all_similar, keyword.replace(" ", "_"))
                    print(status)
                except:
                    continue
        conn.close()

    print(1)

