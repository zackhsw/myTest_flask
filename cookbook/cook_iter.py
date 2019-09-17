# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)  # ython的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象。
#
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     # Outputs Node(1), Node(2)
#     for ch in root:
#         print(ch)

# 使用生成器创建新的迭代模式
# def frange(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
#
#
# if __name__ == '__main__':
#     for n in frange(0, 4, 0.5):
#         print(n)

# 实现迭代器协议
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         使得类变的可迭代
#         return iter(self._children)
#
#     def depth_first(self):
#         yield self
#         for c in self:
#             yield from c.depth_first()
#
#
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     child1.add_child(Node(3))
#     child1.add_child(Node(4))
#     child2.add_child(Node(5))
#
#     for ch in root.depth_first():
#         print(ch)

# 带外部状态的生成器函数

# 迭代器切片
# def count(n):
#     while True:
#         yield n
#         n += 1
#
# c = count(0)
# import itertools
# for x in itertools.islice(c,10,20):
#     print(x)

# items = [1,2,3]
# it = iter(items)
# print(next(it))
# print(next(it))
# print(next(it))

# 同时迭代多个序列
# xpts = [1, 5, 4, 2, 10, 7]
# ypts = [101, 78, 37, 15, 62, 99]
# for x, y in zip(xpts, ypts):
#     print(x, y)
#
# for i in zip(xpts, ypts):
#     print(i)
#
# a = [1, 2, 3]
# b = ['w', 'x', 'y', 'z']
# from itertools import zip_longest
# for i in zip_longest(a, b, fillvalue=0):
#     print(i)
#
# print(list(zip(a, b)), dict(zip(a, b)))
# # zip() 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 list() 函数。

# # 不同集合上的元素迭代
# from itertools import chain
# # 对 a b 进行相同方式迭代，及时a b 中数据类型不同
# a = [1,2,3,4]
# b=['x','y','z']
# # 如果输入序列非常大的时候 chian()会很省内存。 并且当可迭代对象类型不一样的时候
# for x in chain(a,b):
#     print(x)

# 展开多层嵌套，变成单层
# from collections import Iterable
#
#
# def flatten(items, ignore_type=(str, bytes)):
#     for x in items:
#         # 额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，防止将它们再展开成单个的字符。
#         if isinstance(x, Iterable) and not isinstance(x, ignore_type):
#             yield from flatten(x)
#         else:
#             yield x
#
#
# items = [1, 2, [3, 4, [5, 6], 7], 8]
# for x in flatten(items):
#     print(x)

# 顺序迭代合并后的排序迭代对象
# import heapq
#
# a = [1, 4, 7, 10]
# b = [2, 5, 6, 11]
# # heapq.merge() 需要所有输入序列必须是排过序的。
# # 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。
# for c in heapq.merge(a, b):
#     print(c)

# 迭代器代替while

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        # process_data(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
