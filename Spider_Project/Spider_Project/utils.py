import requests

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.163 Safari/537.36',
}


class AppConfig:

    # 根据不同类型，返回相似图或rimg对应的data结构和url
    def params_parse(self, type):
        typedict = {'similar': "HoAMBc", "rimg": "phEE8d"}
        params = {
            "rpcids": "",
            "f.sid": "-5078489349676083701",
            "bl": "boq_visualfrontendserver_20200426.22_p0",
            "hl": "en",
            "authuser": "0",
            "rt": "c"
        }
        baseurl = 'https://www.google.com/_/VisualFrontendUi/data/batchexecute'
        params['rpcids'] = typedict[type]

        return params, baseurl

    def google_origdata_proper(self, keyword):
        orig_params = {
            'ei': 'nIsVXuX7ENuXr7wPhZCYiAg',
            'rlz': '1C1GIWA_enTW877TW877',
            # 'yv': '3',
            'tbm': 'isch',
            'q': '',  # keyword
            'vet': '10ahUKEwjluaWMxPPmAhXby4sBHQUIBoEQuT0IaigB.nIsVXuX7ENuXr7wPhZCYiAg.i',
            'ved': '0ahUKEwjluaWMxPPmAhXby4sBHQUIBoEQuT0IaigB',
            'ijn': '1',  # pagenum 每页100条数据左右
            'asearch': 'ichunk',
            'async': '_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc',
        }
        orig_url = 'https://www.google.com/search'
        orig_params['q'] = keyword
        return orig_params, orig_url

    # 根据最大数量根据每页100条数据转换page数量，并返回对应页数所有的datalist
    def google_similar_rimg(self, data, key):
        params, reurl = self.params_parse('rimg')
        response = requests.post(reurl, headers=HEADER,
                                 params=params,
                                 data=data)
        try:
            rimg = response.text.split('rimg')[1].split('\\"')[0]
        except Exception as e:
            return e

        similar_data_list = []
        for pnum in range(1, 8):
            frepstr = '[[["HoAMBc","[null,null,[' + str(pnum) + '],\\"\\",\\"rimg' + rimg + '\\",\\"\\",\\"\\",[\\"' + key + '\\",\\"en\\"]]",null,"generic"]]]'
            similar_data = dict()
            similar_data['f.req'] = frepstr
            similar_data_list.append(similar_data)
        return similar_data_list

