# 事件循环+回调（驱动生成器）+ epoll(IO多路复用）
# asyncio 是python用于解决异步io编程的一整套解决方案
# torando(实现web服务器） django flask（需要第三方uwsgi, gunicorn+nginx 实现部署)
# tornado （实现了web服务器）可以直接部署，nginx+tornado 可以一起部署

# 使用asyncio
import asyncio
import time

# 获取协程的返回值
from functools import partial

#
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
#
# def callback(url,future):
#     print(url)
#     print("send email to bobby")
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop= asyncio.get_event_loop()
#     # get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
#     # loop.create_task()
#     task = loop.create_task(get_html("http://www.baidu.com"))
#     task.add_done_callback(partial(callback, "http://www.baidu.ccom"))
#     loop.run_until_complete(task)
    # print(get_future.result())


    # tasks = [get_html("http://www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(time.time() - start_time)


# wait 和 gather

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")

if __name__ == '__main__':
    start_time = time.time()
    loop= asyncio.get_event_loop()
    tasks = [get_html("http://www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time() - start_time)

    # gather 和 wait的区别
    # gather 更加 high-level， 开发的时候可以优先考虑gather方法
    group1 = [get_html("http://www.baidu.com") for i in range(2)]
    group2 = [get_html("http://www.baidu.com") for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group2.cancel()  # 也可以取消，
    loop.run_until_complete(asyncio.gather(group1,group2))  # 将俩任务分别传入
    # loop.run_until_complete(asyncio.gather(*group1,*group2))  # 将俩任务分别传入
    print(time.time() - start_time)