# 什么是迭代器
# 迭代器是访问集合内元素的一种形式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能反悔的，迭代器提供了一种惰性访问数据的方式
# [] list, 可迭代的 都是实现了"迭代协议" __iter__()
from collections.abc import Iterable, Iterator
a = [12,11]
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))

print(isinstance(a,Iterable))
print(isinstance(iter(a),Iterator))  # 转成迭代器

