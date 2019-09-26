# 通过queue的方式进行线程同步

from queue import Queue

# 线程通信

import threading
import time


def get_detail_html(queue):
    # 爬取文章详细页
    while True:
        print("get detail html started")
        # if queue.empty():
        #     break
        url = queue.get()  # 如果队列为空 会阻塞在这
        print(f"html {url}")
        time.sleep(1)
        print("get detail html end")


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(1)
        for i in range(5):
            queue.put("http://project.com/{id}".format(id=i))
        print("get detail url end")


# 2.线程通信方式：Queue 是线程安全的，首选线程间通信方式（因为使用了锁机制，和dequeue双端队列这个本身是线程安全的）
# 参考：http://c.biancheng.net/view/2624.html
if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    thread1 = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    start_time = time.time()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    thread1.start()

    detail_url_queue.task_done()  # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    detail_url_queue.join()  # 实际上意味着等到队列为空，再执行别的操作
    print("last time: {}".format(time.time() - start_time))
