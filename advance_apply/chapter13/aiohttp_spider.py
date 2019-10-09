# asyncio爬虫、去重、入库
# 如果需要并发http请求怎么办呢，通常是用requests，但requests是同步的库，如果想异步的话需要引入aiohttp。
# 这里引入一个类，from aiohttp import ClientSession，首先要建立一个session对象，然后用session对象去打开网页。
# session可以进行多项操作，比如post, get, put, head等。
# 基本用法：
# async with ClientSession() as session:
#     async with session.get(url) as response:
# https://www.cnblogs.com/shenh/p/9090586.html
import asyncio
import re

import aiohttp
import aiomysql

from pyquery import PyQuery

start_url = "https://juejin.im/"
# start_url = "http://www.jobbole.com/"
waiting_urls = []
seen_urls = set()
stopping = False


async def fetch(url, session):
    try:
        async with session.get(url) as resp:
            print("url status:{}".format(resp.status))
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
    except Exception as e:
        print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waiting_urls.append(url)
    return urls


async def init_urls(url,session):
    html = await fetch(url,session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = f"insert into article_test(title) values('{title}')"
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print(f"start get url {url}")
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
                    await asyncio.sleep(2)
            # else:
            #     if url not in seen_urls:
            #         asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, user='root', password='passwd', db='aiohttp_test',
                                      loop=loop,
                                      charset='utf8', autocommit=True)

    # asyncio.ensure_future(init_urls(start_url))

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
