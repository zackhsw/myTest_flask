from advance_apply.chapter04.class_method import Date
class User:
    def __init__(self,birthday):
        self.__birthday = birthday  # 双下划綫对属性变量进行私有化

    def get_age(self):
        return 2019 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1990,2,1))
    # print(user.__birthday)  # 无法访问
    print(user._User__birthday)  # 但这样可以访问，对于java 有private 变量也是可以拿到的只不过比较复杂，所以没有绝对私有安全
    print(user.get_age())