class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()

# 既然重写了B的构造函数，为什么还要调用super？

# super的调用顺序是什么样的

if __name__ == '__main__':
    b = B()
