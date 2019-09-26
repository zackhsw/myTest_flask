import threading
from threading import Lock, RLock

# Lock 中不能引入多个acquire 和多个release ,因此引入RLock 可重入锁
# RLock在同一个线程里面，可以连续调用多次acquire,一定要注意acquire次数和release次数相等

total = 0
# lock = Lock()
lock = RLock()  # 锁中这个使用的比较多
def add():
    global total
    global lock
    for i in range(100000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(100000):
        lock.acquire()
        total -= 1
        lock.release()

# 如web 电子商城 多个用户（多个线程）抢同一商品，这是需要线程同步
""" dis查看字节码执行过程
1.load total
2.load 1
3. +
4. 赋值给total
这个过程每一步骤间都有可能被打断 切到desc方法线程的减操作，
尤其最后一步 赋值会出问题
"""

# 所以使用python提供的锁Lock,

# 1.Lock会影响程序的并发性能。
# 2.Lock会引起死锁。

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)