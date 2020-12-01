import logging
import requests
import os

logger = logging.getLogger('MainConnect.ImageDownload')


def save_img(url, savename, imgnums, progress):
    if not os.path.exists(os.path.dirname(savename)):
        os.makedirs(os.path.dirname(savename))
    res = requests.get(url, timeout=(3, 10))
    with open(savename, 'wb') as fp:
        fp.write(res.content)
    logger.info(savename + "   save success##" + str(int(progress // imgnums)))


class MainDownload:
    def __init__(self, key_urls_dict, savepath):
        """
        :param key_urls_dict: {key: ((url1), (url2), (), ()...)
        :param savepath: 保存路径
        :param queues: 队列数
        """
        self.key_urls_dict = key_urls_dict
        self.savepath = savepath

    def google_url_deal(self):
        dst_values = list()
        for keyword in self.key_urls_dict:
            savepath = self.savepath + "\\" + keyword
            dst_values.extend([[value[0], savepath + "\\" + str(index) + ".jpg"]
                               for index, value in enumerate(self.key_urls_dict[keyword])])
        return dst_values

    def googlemain(self):
        progress = 0
        new_values = self.google_url_deal()
        nums = len(new_values)
        for value in new_values:
            progress += 1
            url, savename = value
            save_img(url, savename, nums, progress)

