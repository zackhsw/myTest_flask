# partial 偏函数
# def output_result(result, log=None):
#     if log is not None:
#         log.debug("Got:%r", result)
#
#
# def add(x, y):
#     return x + y
#
#
# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial
#
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')
#
#     p = Pool()
#     p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
#     p.close()
#     p.join()

# from urllib.request import urlopen
#
# # 对单一方法类，来达到存储某些额外状态的方法，可以是有闭包的方案更加简洁
# # 单一方法类转换为函数
# class UrlTemplate(object):
#     def __init__(self, template):
#         self.template = template
#
#     def open(self, **kwargs):
#         return urlopen(self.template.format_map(kwargs))
#
#
# def urltemplate(template):
#     def opener(**kwargs):
#         return urlopen(template.format_map(kwargs))
#     return opener
#
#
# # yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# # for line in yahoo.open(names='IBM,AAPL,FB',fields='silclv'):
# #     print(line.decode('utf-8'))
# yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo(names='IBM,AAPL,FB', fields='sllclv'):
#     print(line.decode('utf-8'))


# # 带额外状态信息的回调函数
# def apply_async(func, args, *, callback):
#     result = func(*args)
#     callback(result)
#
#
# def print_result(result):
#     print('Got:', result)


# def add(x, y):
#     return x + y
#
#
# # apply_async(add, (2, 3), callback=print_result)
#
# # 使用类的形式作为回调函数
# # class ResultHandler:
# #     def __init__(self):
# #         self.sequence = 0
# #
# #     def handler(self, result):
# #         self.sequence += 1
# #         print('[{}] got:{}'.format(self.sequence, result))
# #
# #
# # r = ResultHandler()
# # result = apply_async(add, (2, 3), callback=r.handler)
#
#
# # 使用闭包作为回调函数
# # def make_handler():
# #     sequence = 0
# #
# #     def handler(result):
# #         nonlocal sequence
# #         sequence += 1
# #         print('[{}] Got: {}'.format(sequence, result))
# #
# #     return handler
# #
# #
# # handler = make_handler()
# # apply_async(add, (2, 3), callback=handler)
# # apply_async(add, (2, 3), callback=handler)
#
#
# def make_handler():
#     sequence = 0
#     while True:
#         result = yield
#         sequence += 1
#         print('[{}] yield Got: {}'.format(sequence, result))
#
#
# handler = make_handler()
# print(next(handler))
# apply_async(add, (2, 3), callback=handler.send)

# def h():
#     print('Wen Chuan')
#     # yield 5
#     ret = yield 6
#     print('after')
#     print(f'second---{ret}!')
#
# c = h()
# print(next(c))
# # print(next(c))
# print(c.send(7))  # send() 方法里包含next()方法 会输出yield 后面的值 （这个说法不严谨）


# def foo(num):
#     print("starting...")
#     while num < 10:
#         num = num + 1
#         yield num
#
# print(type(foo(8)))
# print([i for i in foo(2)])  # 这里foo(2) 返回的就是个生成器
# for n in foo(0):  # for循环中完成 foo(0).next() 的步骤
#     print(n,type(n))

# 内联回调函数 通过使用生成器和协程可以使得回调函数内联在某个函数中
# def apply_async(func, args, *, callback):
#     result = func(*args)
#     callback(result)
#
#
# from queue import Queue
# from functools import wraps
#
#
# class Async:
#     def __init__(self, func, args):
#         self.func = func
#         self.args = args
#
#
# def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#         f = func(*args)
#         result_queue = Queue()
#         result_queue.put(None)
#         while True:
#             result = result_queue.get()
#             try:
#                 a = f.send(result)
#                 apply_async(a.func, a.args, callback=result_queue.put)
#             except StopIteration:
#                 break
#
#     return wrapper
#
#
# def add(x, y):
#     return x + y
#
#
# @inlined_async
# def test():
#     r = yield Async(add, (2, 3))
#     print(r)
#     r = yield Async(add, ('hello ', 'world'))
#     print(r)
#     for n in range(10):
#         r = yield Async(add, (n, n))
#         print(r)
#     print('goodbye')
#
#
# if __name__ == '__main__':
#     import multiprocessing
#
#     pool = multiprocessing.Pool()
#     apply_async = pool.apply_async(test())
#     # test()

# 访问闭包中的定义的变量，扩展函数中某闭包，允许它能访问 修改函数的内部变量
# def sample():
#     n = 0
#
#     def func():
#         print('n', n)
#
#     def get_n():
#         return n
#
#     def set_n(value):
#         nonlocal n
#         n = value
#
#     func.get_n = get_n
#     func.set_n = set_n
#     return func
#
# f = sample()
# print('aaa',f.get_n())
# f.set_n(10)
# print('bbb',f())
# print('ccc',f.get_n())


# def push_notify(a, b=0):
#     if isinstance(b, int):
#         b = str(b)
#     for i in b:
#         print('for---', i)
#     print(a, b)
#
#
# push_notify(1, [2, 3])
# push_notify(1, 2)

# @contextmanager
from contextlib import contextmanager


@contextmanager
def make_context():
    print("enter")
    try:
        print("try - in ")
        yield {}
    except RuntimeError as err:
        print('error', err)
    finally:
        print("exit")


with make_context() as value:
    print(value,type(value))
    # pass
