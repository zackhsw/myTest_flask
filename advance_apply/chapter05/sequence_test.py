from collections import abc

a = [1, 2]
c = a + [3, 4]
print(c)  # [1, 2, 3, 4]

# 原地加
# a += [3, 4]
# print(a)  # [1, 2, 3, 4]
#
# a.extend(range(3))  # extend没有返回值
# print(a)  # [1, 2, 3, 4, 0, 1, 2]
a.append([1,2])
print(a)  # [1, 2, [1, 2]]
