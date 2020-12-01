import requests
from bs4 import BeautifulSoup
import json
from DB_Script_Deal import DealWithDB
from Generic_Download.Main_Download import MainDownload
from utils import AppConfig
import logging
import math

logger = logging.getLogger('MainConnect.GoogleImageParse')
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.163 Safari/537.36',
}


class GoogleImageParse(DealWithDB):
    def __init__(self, config):
        super().__init__()
        self.keyword = config['keywords']
        self.savepath = config['savepath']
        self.queues = config['queues']
        self.maxnum = config['maxnum']
        self.similar = config['similar']
        self.action = config['action']
        self.utils = AppConfig()
        self.table_list = [(keyw, "Google_" + keyw.replace(' ', '_'))
                           for keyw in self.keyword]

    # 根据关键词，最大图片数获取图片连接，并返回tablename和图片链接list
    def accor_key_get_orig_url(self, para, maxnum, keyword, url):
        #  结构 ： [[url, simdata], []]
        todb = list()

        #  每个关键词最大页数， 每页100条
        for ijn in range(1, 9):
            para['ijn'] = ijn
            try:
                response = requests.get(url, params=para, headers=HEADER)
                soup = BeautifulSoup(response.text, 'lxml')
                orig_urls = soup.find_all("div", class_="rg_meta notranslate")
            except:
                logger.exception("original request erro ", exc_info=True)
                continue

            for orig_url in orig_urls:
                # orig的图片url数量大于最大数量就跳出循环
                if len(todb) > maxnum:
                    break
                freq = '[[["phEE8d","[null,\\"imgdii\\",\\"docid\\",null,383,null,null,null,false,[\\"key\\"],null,null,false,0,false]",null,"1"]]]'
                url_js = json.loads(orig_url.text)
                ou_url = url_js['ou']
                data = freq.replace("imgdii", url_js['id']).replace("docid", url_js['rid']).replace("key", keyword)
                todb.append([ou_url, data])
        if not todb:
            return False
        else:
            logger.info(keyword + '  original url parse success !!!')
            return todb

    # 根据相似图data，和最大页数，返回可以解析rimg的链接list
    def parse_similar_image(self, rimg_data, keyword, maxnum):
        """  :return  [[url, similardata], []]"""
        param, url = self.utils.params_parse('similar')
        resp = requests.post(url, params=param, headers=HEADER, data=rimg_data)
        if resp.status_code != 200:
            return False
        todb = list()
        url_texts = resp.text.split('[1,[0,\\"')
        for urltext in url_texts:
            if len(todb) >= int(maxnum):
                return todb
            if "HoAMBc" in urltext:
                continue
            else:
                freq = '[[["phEE8d","[null,\\"imgdii\\",\\"docid\\",null,383,null,null,null,false,[\\"key\\"],null,null,false,0,false]",null,"1"]]]'

                lsd = urltext.split('\\",[\\"http')
                imgdii = lsd[0]
                imgurl = 'http' + lsd[1].split('\\n,[\\"http')[1].split('\\"')[0]
                docid = lsd[1].split('\\"2003\\":[')[1].split(',')[1].strip('\\"')
                data = freq.replace("imgdii", imgdii).replace("docid", docid).replace("key",
                                                                                                             keyword)
                todb.append([imgurl, data])
        logger.info('one orig url parse %d similar urls success ', len(todb))
        return todb

    def insert_todb(self, values, table):
        # create table with the keyword remove the space
        self.create_table(table)
        insertstat = self.insert_to_sq(values, table)
        logger.info(insertstat)

    def run_orig_and_insert(self, maxnum):
        for (key, keytable) in self.table_list:
            keypara, url = self.utils.google_origdata_proper(key)
            values = self.accor_key_get_orig_url(keypara, maxnum, key, url)
            if values is False:
                logger.error(key + ' original url parse Failed !!!')
                continue
            else:
                self.insert_todb(values, keytable)

    def run_similar_and_insert(self, maxnum):
        for (key, keytable) in self.table_list:
            orig_datas = self.search_db(keytable)

            for str_data in orig_datas:
                # print(str_data[0], str_data[0].replace("'", '"'))
                # # 存到数据库中时不能字典，直接用str，出现单引号
                orig_js_data = {"f.req": str_data[0]}
                rimg_datalist = self.utils.google_similar_rimg(orig_js_data, key)
                if not isinstance(rimg_datalist, list):
                    logger.info(rimg_datalist)
                    continue
                for rimg_data in rimg_datalist:
                    values = self.parse_similar_image(rimg_data, key, maxnum)
                    if not isinstance(values, list):
                        logger.error("Similar urls get Failed!!!")
                    if len(values) >= maxnum:
                        self.insert_todb(values, keytable)
                        break
                    self.insert_todb(values, keytable)

    def main(self):
        if self.similar:
            maxnum = int(math.sqrt(int(self.maxnum)))
            # 图片下载函数
            if self.action == 2:
                downdict = dict()
                for (key, keytable) in self.table_list:
                    urls = self.download_url_dbsearch(keytable)
                    downdict[key] = urls
                logger.info("Starting to Download from Google DB ..............")
                MainDownload(downdict, savepath=self.savepath).googlemain()

            else:
                logger.info("Starting insert to Google DB ..............")
                self.run_orig_and_insert(maxnum)
                logger.info('original url insert success')
                self.run_similar_and_insert(maxnum)
                logger.info('All URL Insert success')
                # 图片下载函数
                if self.action == 0:
                    downdict = dict()
                    for (key, keytable) in self.table_list:
                        urls = self.download_url_dbsearch(keytable)
                        downdict[key] = urls
                    logger.info("Starting to Download from Google DB ..............")
                    MainDownload(downdict, savepath=self.savepath).googlemain()
        else:
            if self.action == 2:
                downdict = dict()
                for (key, keytable) in self.table_list:
                    urls = self.download_url_dbsearch(keytable)
                    downdict[key] = urls
                logger.info("Starting to Download from Google DB ..............")
                MainDownload(downdict, savepath=self.savepath)
            else:
                logger.info("Starting insert to Google DB ..............")
                self.run_orig_and_insert(self.maxnum)
                logger.info('original url insert success')
                # 图片下载函数
                if self.action == 0:
                    downdict = dict()
                    for (key, keytable) in self.table_list:
                        urls = self.download_url_dbsearch(keytable)
                        downdict[key] = urls
                    logger.info("Starting to Download from Google DB ..............")
                    MainDownload(downdict, savepath=self.savepath)
        logger.info('All Finished。。。')


