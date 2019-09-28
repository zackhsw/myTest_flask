# 1.回调模式编码复杂度高
# 2.同步编程的并发性不高
# 3.多线程编程需要线程间同步，lock

# 1.采用同步的方式去编写异步的代码
# 2.使用单线程去切换任务
#     1.线程是有操作系统切换的，单线程切换意味着我们需要程序员自己去调度任务
#     2.不在需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高


# 传统函数调用，过程 A-->B--> C
# 协程会暂挂起函数，进入到另一个函数去执行，可以暂停的函数（可想暂停的函数传入参数）

def gen_func():
    # 1.可以产出值，2.可以接收值（调用方法传递进来的值）
    html = yield "http://www.baidu.com"
    print("func--", html)
    yield 2
    yield 3
    return "ending"

# throw,close
# 1.生成器不只可以产出值，还可以接收值

if __name__ == '__main__':
    gen = gen_func()
    url = next(gen)
    print("main--", url)
    html = "send net.."
    # 在调用send发送之前，必须启动一次生成器，方式两种：1. gen.send(None), 2. next(gen)。否则不会执行到yield 而抛出异常
    aa = gen.send(html)  # send方法可以传递至进入生成器内部，同时还可以重启生成器执行到下一个yield的位置
    # 1.启动生成器方式有两种：next()和 send()
    print(aa)
    # print(next(gen))
