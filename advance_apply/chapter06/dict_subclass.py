# 不建议继承list和dict
class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = MyDict(one=1)  # 继承的重写的__setitem__没有生效
my_dict["one"] = 1  # {'one': 2}
print(my_dict)

from collections import UserDict


class MyDict(UserDict):  # UserDict重写了c语言的部分
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)
my_dict = MyDict(one=1)  # 生效
print(my_dict)

from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["bbbb"]  # {}  是__missing__实现的 也方便自定义实现
print(my_value)