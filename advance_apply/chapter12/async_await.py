# python为了将语义变得更加明确，就引入了async await两个关键词用于定义原生的协程

async def downloader(url):
    return "jack"
async def download_url(url):
    html = await downloader(url)
    return html

if __name__ == '__main__':
    coro = download_url("http://www.baidu.com")
    coro.send(None)