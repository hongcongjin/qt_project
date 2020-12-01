import aiohttp
from queue import Queue
import asyncio
import logging
import os

logger = logging.getLogger('MainConnect.ImageDownload')


async def makdirs(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


async def get_res(url, savedir):
    """
    :param url: 待请求的url
    :param type: 需要返回的类型，包含content， text
    :return: 根据类型返回对应的结果
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url, verify_ssl=False) as response:
            assert response.status == 200
            if savedir:
                await makdirs(savedir)
            content = await response.read()
            return content


class AsyncGrab:

    def __init__(self, req_urls, max_threads, imagenums):
        """
        :param req_urls: [[url, savename], [url1, savename2], ]
        :param max_threads:
        :param imagenums: the nums of all images
        """
        self.req_urls = req_urls
        self.max_threads = max_threads
        self.imgnums = imagenums
        self.progress = 1

    def __save_img(self, content, savename):
        with open(savename, 'wb') as fp:
            fp.write(content)
        logger.info(savename + "   save success##" + str(int(self.progress // self.imgnums)))

    async def get_results(self, urllist):

        url, savename = urllist
        res = await get_res(url, os.path.dirname(savename))
        self.__save_img(res, savename)
        return "Completed"

    async def handler_tasks(self, task_id, work_queue):
        while not work_queue.empty():
            current_url = work_queue.get()
            try:
                taskstatus = await self.get_results(current_url)
            except Exception as e:
                logging.exception("Erro for {}".format(current_url), exc_info=True)

    def event_loop(self):
        q = Queue()
        [q.put_nowait(urllist) for urllist in self.req_urls]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # selector = selectors.SelectSelector()
        # loop = asyncio.SelectorEventLoop(selector)
        # asyncio.set_event_loop(loop)
        # loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(self.handler_tasks(task_id, q)) for task_id in range(self.max_threads)]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()


