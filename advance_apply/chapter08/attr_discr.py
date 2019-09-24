import numbers
from datetime import date, datetime


# 实现这三个魔法函数就是属性描述符
class IntField(object):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 非数据描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()


if __name__ == '__main__':
    user = User()
    user.age = 20  # 调用了类中的属性描述符的 __set__ 方法
    print(user.age)
    print(getattr(user,"age"))  # 同上等价，首先调用__getattribute__ ,若抛出异常 就会调用定义了的__getattr__
    # user.age = "asd2"  # ValueError: int value need
