from multiprocessing import Process, Queue, Pool, Manager,Pipe
# from queue import Queue  # 多进程通信应使用上multiprocessing提供的Queue
import time


# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)

def producer(pipe):
    pipe.send("hello pipe")


def consumer(pipe):
    print(f"consumer {pipe.recv()}")


# 1.共享变量，不适用于多进程（但适合多线程），多进程中的数据是完全隔离的
# 2.multiprocessing 中的Queue不能用于pool进程池, 但可以使用Manager 使进程池中的进程通信
# 3. Pipe使进程间通信,但只能适用于两个进程, Pipe的性能要高于Queue
if __name__ == '__main__':

    receive_pip, send_pipe = Pipe()
    # pipe 只能适用于两个进程
    my_producer = Process(target=producer,args=(send_pipe,))
    my_consumer = Process(target=consumer,args=(receive_pip,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

    # queue = Manager().Queue(10)
    # pool = Pool(2)
    # pool.apply_async(producer, args=(queue,))
    # pool.apply_async(consumer, args=(queue,))
    # pool.close()
    # pool.join()

    # 下面进程不能执行。multiprocessing 中的Queue不能用于pool进程池
    # queue = Queue(10)
    # my_producer = Process(target=producer,args=(queue,))
    # my_consumer = Process(target=consumer,args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

def add_data(p_dict,key,value):
    p_dict[key] = value

if __name__ == '__main__':
    # 进程同步的方式 有很多和线程方式类似
    # 进程间内存共享方式，也注意同步问题
    progress_dict = Manager().dict()
    first_progress = Process(target=add_data,args=(progress_dict,"aa",11))
    second_progress = Process(target=add_data,args=(progress_dict,"bb",22))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress_dict)  # >> {'aa': 11, 'bb': 22}