# 线程通信

import threading
import time
from advance_apply.chapter11 import variables

# 全局变量（用作共享变量）线程适用这个共享变量的方式，但进程不适合此方式
# detail_url_list = []   # 或者将全局变量放在另一个文件中，就可以不用函数传参的方式，其实另一个文件导入全局变量 也是一种全局变量形式


# def get_detail_html(detail_url_list):
def get_detail_html():
    # 爬取文章详细页
    # global detail_url_list
    while True:
        if len(variables.detail_url_list):
            print("get detail html started")
            url = variables.detail_url_list.pop()
            print(f"html {url}")
            # time.sleep(0.5)
            print("get detail html end")


def get_detail_url():
    # 爬取文章列表页
    # global detail_url_list  # 或者函数传入detail_url_list全局变量 此方式更灵活
    while True:
        print("get detail url started")
        time.sleep(1)
        for i in range(10):
            variables.detail_url_list.append("http://project.com/{id}".format(id=i))
        print("get detail url end")


# 1.线程通信方式：共享变量 （这种方式不是线程安全）所以需要加锁
if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_detail_html, args=(detail_url_list,))
    thread1 = threading.Thread(target=get_detail_url)
    threads_list = []
    for i in range(10):
        # html_thread = threading.Thread(target=get_detail_url, args=(variables.detail_url_list,))
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()
    print(threads_list)
    start_time = time.time()
    thread1.start()
    #
    # thread1.join()  # 阻塞主线程 ，主线程等待thread1执行完
    # for i in threads_list:
    #     i.join()

    print("last time: {}".format(time.time() - start_time))
