# 对于IO,多线程与多进程差别不大
# 1.Thread类实例化
import threading
import time


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html started")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url started")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # 将线程设置为守护线程，将 daemon 属性设为 True，必须在 start() 方法调用之前进行，否则会引发 RuntimeError 异常。
    # 当主线程或其他线程退出/死掉，守护线程也退出（不论守护线程是否执行完毕都退出）
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()  # 阻塞主线程 ，主线程等待thread1执行完
    thread2.join()  # 同上
    print("last time: {}".format(time.time() - start_time))


# 2.通过集成Thread实现多线程 （当逻辑比较复杂的时候,此方法很适用）

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html started")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url started")


if __name__ == '__main__':
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()  # 阻塞主线程 ，主线程等待thread1执行完
    thread2.join()  # 同上
    print("last time: {}".format(time.time() - start_time))
