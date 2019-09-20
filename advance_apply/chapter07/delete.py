# python中垃圾回收的算法采用 引用计数
# a = 1
a = object()
b = a
del a  # 这个对象没有被删除 是a的引用计数减到0
print(b)
print(a)

class A:
    def __del__(self): # 实现删除功能
        pass