# GIL global interpreter lock
# python中一个线程对应c语言中的一个线程，（针对CPython解释器）
# GIL使得同一时刻只有一个线程在一个cpu上执行字节码, 无法多线程映射到多个CPU上去利用多核。
# GIL会根据执行的字节码行数以及时间片释放GIL.GIL会在遇到IO操作主动释放（这一点使python在IO操作上表现良好）
# import dis
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)  # 多次执行发现正负数都有 GIL不能使线程安全