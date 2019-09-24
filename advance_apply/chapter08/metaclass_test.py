# 类也是对象，type创建类的类
# type 可以检查类型，还可以创建类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


# type动态创建类, 包括属性 方法，也可以继承父类
# User = type("User", (), {})

def say(self):
    return "i am user."
    # return self.name


class BaseClass:
    def answer(self):
        return "i am baseclass."


# 什么是元类，元类是创建类的类，对象 <-class(对象) <-type
class MetaClass(type):  # 自定义元类
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    pass


# python中类的实例化过程，首先寻找metaclass,通过metaclass去创建user类
# （不然最后调用）type去创建类对象，实例


if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    User = type("User", (BaseClass,), {"name": "user", "say": say})  # t
    my_obj = User()
    print(my_obj.name)
    print(my_obj.say())
    print(my_obj.answer())
