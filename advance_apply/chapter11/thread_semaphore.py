# Semaphore 是用于控制进入数量的锁
# 文件：读、写，写一般只是用于一个线程写，读可以允许多个线程读

# 爬虫，
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        # time.sleep(2)
        print("go html text success")
        self.sem.release()  # 执行一次 信号量计数加一


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()  # 每次调用使Semaphore内部计数减一 减到0，此线程阻塞，等待信号量计数大于0
            print("hh")
            html_thread = HtmlSpider("http://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)  # 内部使用了Condition
    url_producer = UrlProducer(sem)
    url_producer.start()
