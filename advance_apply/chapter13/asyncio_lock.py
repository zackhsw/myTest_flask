import asyncio
from asyncio import Lock, Queue

import aiohttp as aiohttp

cache = {}
lock = Lock()
queue = Queue  # 这个可以设置最大长度

# await queue.get()   # 使用方式

async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET',url)
        cache[url] = stuff
        return stuff

async def parse_stuff():
    stuff = await get_stuff()

async def use_stuff():
    stuff = await get_stuff()

tasks = [parse_stuff(), use_stuff()]