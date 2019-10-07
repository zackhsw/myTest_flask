# asyncio爬虫、去重、入库
import asyncio
import re

import aiohttp
import aiomysql

from pyquery import PyQuery

start_url = "http://www.jobbole.com/"
