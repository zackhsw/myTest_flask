class D(object):
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B,C):
    name = "GA"
    def __init__(self):
        self.name = "obj"
# c3算法
a = A()
print(a.name)
print(A.__mro__)  # 可以查到 查询类的顺序 从左到右