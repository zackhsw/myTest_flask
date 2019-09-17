# 自省是通过一定的机制查到对象的内部结构

class Person:
    """ 人"""
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = ""


if __name__ == '__main__':
    user = Student("cccdt")

    # __dict__查询属性
    print(Person.__dict__)
    print(Student.__dict__)
    user.__dict__["school_name"] = "天天"
    print(user.__dict__)
    print(user.school_name)
    print(user.name)  # 会根据mro 向上查询 找到name

    print(dir(user))  # dir功能比__dict__更强大，能看到更多的魔法函数