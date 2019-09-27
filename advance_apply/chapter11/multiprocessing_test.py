import os
import time

# fork只能用于linux、unix中
# 每个进程的资源是完全隔离的，进程间通信并不像线程间通信那么容易
# pid = os.fork()  # AttributeError: module 'os' has no attribute 'fork'
# print("Jack")
# if pid == 0:
#     print(f"子进程 {os.getpid()}, 父进程：{os.getppid()}")
# else:
#     print(f"I am ppid :{pid}")
#
# time.sleep(2)


from concurrent.futures import ProcessPoolExecutor  # 是以multiprocessing为基础的
import multiprocessing

# 多进程编程
import time


def get_html(n):
    time.sleep(n)
    print(f"sub_progress success")
    return n


class MyProgress(multiprocessing.Process):  # 继承的实现方式
    def run(self):
        pass


if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(f"ppid {progress.pid}")
    # progress.start()
    # print(f"ppid {progress.pid}")
    # progress.join()
    # print(f"main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html,args=(3,))

    # pool.close()
    # # 等待所有任务完成
    # pool.join()
    # print(result.get())

    # imap
    # for result in pool.imap(get_html, [1,5,3]):
    #     print(f"{result} sleep success")
    # with Pool() as pool:
    #     iter = pool.imap(func, iter)
    #     for ret in iter:
    # # do something


    for result in pool.imap_unordered(get_html, [1,5,3]):
        print(f"{result} sleep success")
