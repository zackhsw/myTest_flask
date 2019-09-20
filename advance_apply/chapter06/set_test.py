# set 集合fronzenset(不可变集合) 无序 不重复
# s = set("abcde")  # {'c', 'b', 'a', 'd', 'e'}
s = set(['a', 'b', 'c', 'd', 'e'])  # {'d', 'b', 'e', 'a', 'c'}
print(type(s))

s.add('f')
print(s)  # {'e', 'a', 'd', 'c', 'b', 'f'}

# fs = frozenset("abcde")  # fronzeset 可以作为dict的key
# print(fs)

# 向set添加数据
another_set = set("def")
s.update(another_set)
print(s)

# | & - 集合运算 很有用 set 性能很高
re_set = s.difference(another_set)  # 集合差集操作
re_set = s - another_set # 同上 差集
re_set = s & another_set
re_set = s | another_set

print(re_set)

print(s.issubset(re_set))  # 判断是否存在 是否是子集
# if "c" in re_set:
#     print("yes ")

# 1. dict的key或者set的值，都是必须可以hash的
# 不可变对象都是可hash的，str,fronzeset,tuple 自己实现的类 __hash__
# 2. dict的内存开销大（事先分配大空间，一定程度上可避免哈希冲突），但是查询速度快，自定义的对象 或者python内部的对象都是用dict包装的
# 3. dict的存储顺序和元素添加顺序有关 （参照哈希表存放原理）
# 4. 添加数据有可能改变已有的数据顺序  （背后是哈希表实现原理，当插入数值时 可能会改变原有的顺序）