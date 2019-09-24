from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.__age = 0

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property
    def age(self):  # 使得方法变成属性的方式
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self.__age = value


print(f"in {__file__} file")  # 输入当前文件的路径
if __name__ == '__main__':
    user = User("jack", date(year=2000, month=1, day=11))
    # print(user.get_age())
    user.__age = 90
    print(user._age)
    print(user.age)
