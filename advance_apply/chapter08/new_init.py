# __new__在 __init__之前调用
# __new__控制对象的生成过程,应返回实例。 __init__用来完善对象
# 如果__new__不返回对象，就不调用__init__函数
class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
    def __init__(self,name):
        self.name = name
        print("in init")

if __name__ == '__main__':
    user = User("bbb")  # in new
