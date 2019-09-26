import threading
from threading import Condition


# 条件变量，用于复杂的多线程,通过此线程通信 协调各线程

# Lock锁机制 只是锁住了共享变量，不能协调线程的执行
# class AA(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="jack")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : hello rose".format(self.name))
#         self.lock.release()
#
#
# class BB(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="rose")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}: hi jack".format(self.name))
#         self.lock.release()

class AA(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="jack")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : hello rose".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : where are we going to eat?".format(self.name))
            self.cond.notify()

class BB(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="rose")
        self.cond = cond

    def run(self):
        with self.cond :
            print("{}: hi jack".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: hi jack".format(self.name))
            self.cond.notify()
            self.cond.wait()

if __name__ == '__main__':
    # lock = threading.Lock()
    cond = Condition()
    aa = AA(cond)
    bb = BB(cond)
    # 调用时 启动顺序很重要
    # 先调用with cond 再调用notify wait
    # condition有两层锁，一把底层锁会在线程调用了wait方法的时候释放，上面的锁会在每次调用wait方法的时候分配一把锁并放入到cond的等待队列中，等待notify方法唤醒
    # 重点理解Condition中的wait()源码 会助于理解
    aa.start()
    bb.start()
