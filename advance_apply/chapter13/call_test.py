import asyncio

def callback(sleep_time,loop):
    print(f"sleep {sleep_time}; {loop.time()} success")

def stoploop(loop):
    loop.stop()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.call_soon(callback,2) # 即刻执行
    # loop.call_soon(stoploop,loop)
    now = loop.time()
    loop.call_at(now+2,callback,2,loop)
    loop.call_at(now+1,callback,1,loop)
    loop.call_at(now+3,callback,3,loop)
    # loop.call_later(2, callback,2)
    # loop.call_later(1, callback,1)
    # loop.call_later(3, callback,3)
    # loop.call_soon(callback,4)
    loop.call_soon(callback,4,loop)
    loop.run_forever()
