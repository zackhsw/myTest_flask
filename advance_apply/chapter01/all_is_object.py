# python 一切皆对象，包括类 函数 库 包都是对象
#
def ask(name="bbb"):
    print(name)


class Person:
    def __init__(self):
        print("bbby")


def print_type(item):
    print(type(item))


def decorator_func():
    print("dec start")
    return ask


my_ask = decorator_func()  # 将ask方法赋值my_ask
my_ask("tom")

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())
# >>>
# bbb
# None  # 函数没有返回值 故返回为None
# bbby
# <__main__.Person object at 0x000001E3C046DC88>

# my_func = ask  # 印证函数也是对象
# my_func("cccc")

# my_class = Person  # 类作为对象赋值
# my_class()
# # Person()
