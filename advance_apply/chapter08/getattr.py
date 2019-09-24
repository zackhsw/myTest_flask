# __getattr__ 、__getattribute__
# __getattr__ 在查找不到属性的时候调用

from datetime import date, datetime


class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return "bobo"


if __name__ == '__main__':
    user = User("jack", date(year=2000, month=1, day=11), info={"company": "iBMM","address":"usa.xxx"})
    # print(user.age)  # 找不到age ,会调用__getattr__ 方法
    # print(user.address)  # 从__getattr__ 中找item 对应值
    print(user.test)  # 总先调用__getattribute__