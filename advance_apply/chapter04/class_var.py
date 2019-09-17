class A:
    aa = 11  # 类变量 类及所有实例共享 实例修改这变量 相当于创建了一个aa

    def __init__(self, x, y):  # self是类的实例
        self.x = x
        self.y = y

a = A(1,2)
a.aa = 100
print(a.x,a.y,a.aa)  # 1 2 100
print(A.aa)  # aa仍是11
# print(A.x)  # AttributeError: type object 'A' has no attribute 'x'