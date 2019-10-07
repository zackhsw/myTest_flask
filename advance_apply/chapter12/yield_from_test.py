# python3.3新加了yield from语法
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "jack": "http://projectsedu.com",
    "rose": "http://baidu.com"

}


# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         for value in my_iterable:
#             yield value
#
#
# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)

def g1(gen):
    yield from gen


def main():
    g = g1()
    g.send(None)

# 1. main()调用方g1（委托生成器） gen子生成器
# yield from 会在调用方和子生成器之间建立一个双向的通道