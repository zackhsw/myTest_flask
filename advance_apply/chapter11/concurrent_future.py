# 线程池 为什么需要线程池
# 主线程中可以获取一个线程的状态或者某一任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致

# Future , 可看做是task的返回容器，是异步编程的核心，

import time
from concurrent.futures import Future, ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中，submit是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# 要获取已经成功的task的返回值
urls = [1, 8, 4]
all_tasks = [executor.submit(get_html, (url)) for url in urls]
wait(all_tasks, return_when=FIRST_COMPLETED)  # 阻塞主线程，等待满足的设定的条件，FIRST_COMPLETED这个是第一任务完成时执行
print("main")
for future in as_completed(all_tasks):  # as_completed 判断有完成的任务就返回
    data = future.result()
    print(data)

# 通过executor的map获取已经完成的task的值
# for data in executor.map(get_html,urls):
#     print(data)

# print(task1.done())  # done方法用于判定某个任务是否完成 “Return True of the future was cancelled or finished executing”
# print(task2.cancel())  # 取消某任务，成功则返回True
# time.sleep(4)
# print(task1.done())
# print(task1.result()) # result方法可以获取task的执行结果
