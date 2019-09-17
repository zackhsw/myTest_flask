# 任何的序列可以解压同时赋值给多个变量

# 可迭代对象中，赋值给*args变量可动态赋值，接收多个值

# 迭代操作的时候 保留最后几个元素
# from collections import deque
#
#
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
#
# # Example use on a file
# if __name__ == '__main__':
#     with open(r'../../cookbook/somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-' * 20)

# 从集合中获得最大或者最小的N个元素列表
# 对于较大的集合用sorted 或sort 再做切片取N个元素 速度较快些
# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
#
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(cheap,expensive)

# 实现一个优先级队列

# import heapq
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self,item,priority):
#         heapq.heappush(self._queue,(-priority,self._index,item))
#         self._index +=1
#
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
#
# class Item:
#     def __init__(self,name):
#         self.name = name
#
#     def __repr__(self):
#         return "Item({})".format(self.name)
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# print(q.pop())
# print(q.pop())

# 字典一个键对应多个值

# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(3)
# print(d)
#
# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(4)
# print(d)

# 一般的
# pairs = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
# # pairs = [1,  2, 3, 3, 3]
# d = {}
# for key, value in pairs.items():
#     if key not in d:
#         d[key] = []
#     print(key,value)
#     d[key].append(value)
#
# print(d)
#
# # defaultdict方式 实现上述方式更简洁
# from collections import defaultdict
#
# d = defaultdict(list)
# for key, value in pairs.items():
#     d[key].append(value)
# print(d, d['a'], type(d))

# 字典排序
# from collections import OrderedDict
#
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4
# # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
# for key in d:
#     print(key, d[key])

# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
# # w为了对字典值计算，先zip()将键和值反转(zip() 函数创建的是一个只能访问一次的迭代器)
# min_price = min(zip(prices.values(),prices.keys()))
# print(min_price)
# max_price = max(zip(prices.values(),prices.keys()))
# print(max_price)
#
# prices_sorted = sorted(zip(prices.values(),prices.keys()),reverse=True)
# print(prices_sorted)
#
# print(min(prices.values()))
# print(min(prices,key=lambda k: prices[k]))  # 按值查最小，返回键
# print(prices[min(prices,key=lambda k: prices[k])])  # 通过最小值键 返回最小值

# 查找两个字典相同点如键 值

# a = {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }
#
# b = {
#     'w': 10,
#     'x': 11,
#     'y': 2
# }
# # 字典键可做集合操作，items()也是可以，对于值最好转换set 再集合运算
# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(b.keys() - a.keys())
# print(a.items() & b.items())
# print({key:a[key] for key in a.keys() - {'z', 'w'}})

# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)

# a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))

# 消除重复元素
# def dedupe(items, key=None):  # key接收的是lambda表达式
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
#
# a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
# print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
# print(list(dedupe(a, key=lambda d: d['x'])))

# 切片命名
# record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:37])
# print(cost)
# # 使用slice对切片进行命名，方便维护
# SHARES = slice(20, 23)
# PRICE = slice(31, 37)
# cost = int(record[SHARES]) * float(record[PRICE])
# print(cost)

# 序列中出现次数最多的元素
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]
# Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。 在解决这类问题的时候你应该优先选择它
# 还可以做数学运算
# from collections import Counter
# word_counts = Counter(words)
# # 出现频率最高的3个单词
# top_three = word_counts.most_common(3)
# print(top_three)

# 通过关键字排序列表中字典
# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
#
# from operator import itemgetter
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))  # 支持多个key 可以用lambda表达式
# print(rows_by_lfname)
# print(rows_by_fname)
# print(rows_by_uid)

# 排序类型相同的对象，它们不原生支持比较操作

# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
# from operator import attrgetter
# def sort_notcompare():
#     users = [User(23), User(3), User(99)]
#     print(users)
#     print(sorted(users, key=lambda u: u.user_id))
#     print(sorted(users, key=attrgetter('user_id')))  # attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。
#
# sort_notcompare()
# from collections import namedtuple
#
# metro_data = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
#
# LatLong = namedtuple('LatLong', 'lat long')
# Metropolis = namedtuple('Metropolis', 'name cc pop coord')
# metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
#
# from operator import attrgetter
#
# name_lat = attrgetter('name', 'coord.lat')
# for city in sorted(metro_areas,key=attrgetter('coord.lat')):
#     print(name_lat(city))


# 通过某个字段将记录分组
#
# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
#
# from operator import itemgetter
# from itertools import groupby
#
# rows.sort(key=itemgetter('date'))
# # groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(' ', i)

# 过滤序列元素
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# print([n for n in mylist if n > 0])
# print([n for n in mylist if n < 0])
# # 列表推导式潜在危险就是大量结果集 占用大量内存，故可以才有生成器表达式
# pos = (n for n in mylist if n < 0)
# for x in pos:
#     print(x)

# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
# ivals = list(filter(is_int, values))
# print(ivals)

# addresses = [
#     '5412 N CLARK',
#     '5148 N CLARK',
#     '5800 E 58TH',
#     '2122 N CLARK',
#     '5645 N RAVENSWOOD',
#     '1060 W ADDISON',
#     '4801 N BROADWAY',
#     '1039 W GRANVILLE',
# ]
# counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# from itertools import compress
# more5 = [n > 5 for n in counts]
# print(more5)
# # compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
# print(list(compress(addresses,more5)))

# 从字典中提取出子集
# from time import time
#
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# p1 = {key: value for key, value in prices.items() if value > 200}
# print(p1)
# start =time()
# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}
# print(p2)
# end = time()
# print(f"running time: {end-start}")
# # 或者
# p1 = dict((key, value) for key, value in prices.items() if value > 200)
# print(p1)
# start =time()
# tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
# p2 = { key:prices[key] for key in prices.keys() & tech_names }  # 运行时间测试结果显示这种方案大概比第一种方案慢 1.6 倍
# print(p2)
# end = time()
# print(f"2 running time: {end-start}")

# 映射名称到序列元素 collections.namedtuple() 利用可读的下标找到元素

# from collections import namedtuple
# Subscriber = namedtuple('Subscriber',['addr','joined'])
# sub = Subscriber('jsjsj@asdf.com','2019-09-08')
# print(sub,len(sub),sub.addr,sub[0],[i for i in sub],type(sub))
#
# from collections import namedtuple
#
# Stock = namedtuple('Stock', ['name', 'shares', 'price'])
#
#
# # def compute_cost(records):
# #     total = 0.0
# #     for rec in records:
# #         print(rec)
# #         total += rec[1] * rec[2]
# #     return total
# # 命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。
# # 如果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。
# # 但是需要注意的是，不像字典那样，一个命名元组是不可更改的。
# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         s = Stock(*rec)
#         total += s.shares * s.price
#     return total
#
#
# print(compute_cost([['a', 2.0, 3.3],('b', 2.0, 3)]))  # , {'b', 2.0, 3}]

# 转换并计算数据

# nums = [1, 2, 3, 4, 5]
# s = sum(x * x for x in nums)
# print(s)

# 合并多个字典 或映射
#
# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
#
# from collections import ChainMap
#
# c = ChainMap(a, b)  # ChainMap 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表。
# print(c['x'], c,type(c),c['z'],c.parents['z'],c.parents)  # 这里c['z'] 只有a中的值，这只保存第一次出现的值,c.parents['z']出现了b的z映射值

# 两个字典合并
# a = {'x': 1, 'z': 3 }
# b = {'y': 2, 'z': 4 }
# merged = dict(b)  # 但需要额外创建字典 来合并
# merged.update(a)
# print(merged)
# print(merged['x'])
# print(merged['y'])
# print(merged['z'])