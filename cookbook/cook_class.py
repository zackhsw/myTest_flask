# 对象支持上下文协议

# from socket import socket, AF_INET, SOCK_STREAM
#
#
# class LazyConnection:
#     def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
#         self.address = address
#         self.family = family
#         self.type = type
#         self.sock = None
#
#     def __enter__(self):
#         if self.sock is not None:
#             raise RuntimeError("already connected")
#         self.sock = socket(self.family, self.type)
#         self.sock.connect(self.address)
#         return self.sock
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.sock.close()
#         self.sock = None
#
#
# from functools import partial
#
# conn = LazyConnection(('www.python.org', 80))
# # Connection closed
# with conn as s:
#     # conn.__enter__() executes: connection open
#     s.send(b'GET /index.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv, 8192), b''))
#     print(resp)
#     # conn.__exit__() executes: connection closed

# 创建大量对象时节省内存方法
#  使用slots一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在 __slots__ 中定义的那些属性名。
# class Date:
#     __slots__ = ['year', 'month', 'day']
#
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

# 类中封装私有数据 单下划线前缀
# 大多数而言，你应该让你的非公共名称以单下划线开头。但是，如果你清楚你的代码会涉及到子类，
# 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案。
# class B:
#     def __init__(self):
#         self.__private = 0
#
#     def __private_method(self):
#         pass
#
#     def public_method(self):
#         pass
#         self.__private_method()
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.__private = 1 # Does not override B.__private
#
#     # Does not override B.__private_method()
#     def __private_method(self):
#         pass

# 你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证。
# property
# class Person:
#     def __init__(self,first_name):
#         self.first_name = first_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self,value):
#         if not isinstance(value,str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError('can`t delete attribute')
#
# a = Person('jack')
# a.first_name = 55
# print(a.first_name)
# del a.first_name

# 你想在子类中调用父类的某个已经被覆盖的方法。
# 调用父类的方法 super()

# class Base:
#     def __init__(self):
#         print('base.__init__')
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('a.__init__')
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('b.__init__')
#
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print('c.__init__')
#
# c = C()
# print(C.__mro__)  # 方法解析列表MRO

# 子类扩展父类property 功能
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     # Getter function
#     @property
#     def name(self):
#         print('父类 property--')
#         return self._name
#
#     # Setter function
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._name = value
#
#     # Deleter function
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")
#
# class SubPerson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name
#
#     @Person.name.getter
#     def name(self):
#         print('getting name')
#         return super().name
#
#     # @Person.name.setter   # 如果只是想扩展父类的方法
#     # def name(self, value):
#     #     print('Setting name to', value)
#     #     super(SubPerson, SubPerson).name.__set__(self, value)\
#
#     @name.setter
#     def name(self, value):
#         print('Setting name to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)
#
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete__(self)
#
# s = SubPerson('rose')
# print(s.name)

# 一个类实现了__get__、__set__、__delete__其中几个方法，这个类就叫描述器
# 延迟计算属性 将一个只读属性定义成一个property，并且只在访问的时候才会计算结果。但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
#
# class lazyproperty:
#     def __init__(self, func):
#         self.func = func
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance, self.func.__name__, value)
#             return value
#
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @lazyproperty
#     def area(self):
#         print('Computing area')
#         return math.pi * self.radius ** 2
#
#     @lazyproperty
#     def perimeter(self):
#         print('Computing perimeter')
#         return 2 * math.pi * self.radius
#
# c = Circle(4.3)
# print(c.radius)
# print(c.area)
# print(c.area)
# print(c.__dict__)
# print(type(c).__dict__)
# print(c.perimeter)
# print(c.perimeter)
# print(c.area)

# class C:
#     x = 1
#     def __init__(self,y):
#         self.y = y
#
#     def fun(self):
#         print(self.y)
#
# c = C(2)
# print(c.__dict__)
# print(C.__dict__)
# print(type(c).__dict__)
# print(vars(C))

# print(c.fun())
# print(c.__dict__['y'])


# class M:
#     def __init__(self):
#         self.x = 1
#
#     def __get__(self, instance, owner):
#         return self.x
#
#     def __set__(self, instance, value):
#         self.x = value
#
#
# # 调用描述器的类
# class AA:
#     m = M()  # m就是一个描述器
#     n = 2
#
#     def __init__(self, score):
#         self.score = score
#
#
# aa = AA(3)
# print(aa.__dict__)  # {'score': 3}
# print(aa.score)  # 3, 在 aa.__dict__ 中寻找，找到了score直接返回
# print(aa.__dict__['score'])  # 3, 上面的调用机制实际上是这样的
#
# print(type(aa).__dict__)  # 里面有n和m
# print(aa.n)  # 2, 在aa.__dict__中找不到n，于是到type(aa).__dict__中找到了n，并返回其值
# print(type(aa).__dict__['n'])  # 2, 其实是上面一条的调用机制
#
# print(aa.m)  # 1, 在aa.__dict__中找不到n，于是到type(aa).__dict__中找到了m
# # m是一个描述器对象，于是调用__get__方法，将self.x的值返回，即1
# print(type(aa).__dict__['m'].__get__(aa, AA))  # 1, 上面一条的调用方式是这样的
# # __get__的定义中，除了self，还有instance和owner，其实分别表示的就是描述器所在的实例和类，这里的细节我们后文会讲
#
# print('-' * 20)
# print(AA.m)  # 1, 也是一样调用了描述器
# print(AA.__dict__['m'].__get__(None, AA))  # 类相当于调用这个

# class M:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, obj, type):
#         print('get第一个参数self: ', self.name)
#         print('get第二个参数obj: ', obj.age)
#         print('get第三个参数type: ', type.name)
#
#     def __set__(self, obj, value):
#         obj.__dict__[self.name] = value
#
#
# class A:
#     name = 'Bob'
#     m = M('age')
#
#     def __init__(self, age):
#         self.age = age
#
#
# a = A(20)  # age是20
# print(a.m)
# # get第一个参数self:  age
# # get第二个参数obj:  20
# # get第三个参数type:  Bob
# a.m = 30
# print(a.age)  # 30

# 总结如下:
#
# self是描述器类M中的实例
# obj是调用描述器的类a中的实例
# type是调用描述器的类A
# value是对这个属性赋值时传入的值，即上面的30
# 上面的代码逻辑如下
#
# a.m访问描述器，调用__get__方法
# 三次打印分别调用了m.name a.age A.name
# a.m = 30调用了__set__方法，令a(即obj)的属性中的'age'(即M('age')这里传入的self.name)为30

# class B:
#     @classmethod
#     def print_classname(cls):
#         print('Bob')
#
#     @staticmethod
#     def print_staticname():
#         print('my name is bob')
#
#     def print_name(self):
#         print('this name')
#
#
# b = B()
# b.print_classname()  # 调用类方法
# b.print_staticname()  # 调用静态方法
# b.print_name()  # 调用实例方法
# print(B.__dict__)  # 里面有实例方法、静态方法和类方法
# print('*'*20)
# # 但其实字典里的还不是可以直接调用的函数
# print(B.__dict__['print_classname'])
# print(b.print_classname) # 和上不一样
# print(B.__dict__['print_staticname'])
# print(b.print_staticname) # 和上不一样
# print(B.__dict__['print_name'])
# print(b.print_name) # 和上不一样

# class Property(object):
#     "Emulate PyProperty_Type() in Objects/descrobject.c"
#
#     def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#         if doc is None and fget is not None:
#             doc = fget.__doc__
#         self.__doc__ = doc
#
#     def __get__(self, obj, objtype=None):
#         if obj is None:
#             return self
#         if self.fget is None:
#             raise AttributeError("unreadable attribute")
#         return self.fget(obj)
#
#     def __set__(self, obj, value):
#         if self.fset is None:
#             raise AttributeError("can't set attribute")
#         self.fset(obj, value)
#
#     def __delete__(self, obj):
#         if self.fdel is None:
#             raise AttributeError("can't delete attribute")
#         self.fdel(obj)
#
#     def getter(self, fget):
#         return type(self)(fget, self.fset, self.fdel, self.__doc__)
#
#     def setter(self, fset):
#         return type(self)(self.fget, fset, self.fdel, self.__doc__)
#
#     def deleter(self, fdel):
#         return type(self)(self.fget, self.fset, fdel, self.__doc__)


# 装饰器形式，即引言中的形式
# class A:
#     def __init__(self, name, score):
#         self.name = name  # 普通属性
#         self.score = score
#
#     @property
#     def score(self):
#         print('getting score here')
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         print('setting score here')
#         if isinstance(value, int):
#             self._score = value
#         else:
#             print('please input an int')
#
#
# a = A('Bob', 90)
# print(a.name)  # 'Bob'
# print(type(a).__dict__)
# print("--" * 50)
# print(a.score)  # 90
# print("--" * 50)
# a.score = 'bob'  # please input an int
# a.score = 20  # please input an int
# print(a.score)

# class Structure2:
#     _fields = []
#
#     def __init__(self, *args, **kwargs):  # **kwargs可接受关键字参数
#         if len(args) > len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#
#         for name in self._fields[len(args):]:
#             setattr(self, name, kwargs.pop(name))
#
#         if kwargs:
#             raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
#
#
# # Example use
# if __name__ == '__main__':
#     class Stock(Structure2):
#         _fields = ['name', 'shares', 'price']
#
#
#     s1 = Stock('ACME', 50, 91.1)
#     s2 = Stock('ACME', 50, price=91.1)  # 传入关键字参数
#     # s3 = Stock('ACME', shares=50, price=91.1)
#     s3 = Stock('ACME', shares=50, price=91.1, aa=1)
#     print(s1.__dict__, s2.__dict__, s3.__dict__)

# 定义接口和抽象基类 使用abc模块
# from abc import ABCMeta, abstractmethod
#
#
# class IStream(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self, maxbytes=-1):
#         pass
#
#     @abstractmethod
#     def write(self, data):
#         pass
#
#
# a = IStream()  # 这个类不能实例化
#
#
# class SocketStream(IStream):
#     def read(self, maxbytes=-1):
#         pass
#
#     def write(self, data):
#         pass
#
#
# # 抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口：
#
# def serialize(obj, stream):
#     if not isinstance(stream, IStream):
#         raise TypeError('Expected an IStream')
#     pass
#
#
# # 除了继承这种方式外，还可以通过注册方式来让某个类实现抽象基类：
# import io
#
# IStream.register(io.IOBase)
#
# f = open('foo.txt')
# isinstance(f, IStream)
# # 标准库中有很多用到抽象基类的地方。
# # collections 模块定义了很多跟容器和迭代器(序列、映射、集合等)有关的抽象基类。
# # numbers 库定义了跟数字对象(整数、浮点数、有理数等)有关的基类。io 库定义了很多跟I/O操作相关的基类。

# 实现数据类型的

# 实现自定义容器，模拟内置的容器类的功能，使用colletions模块
# import bisect
# import collections
# class SortedItems(collections.Sequence):
#     def __init__(self, initial=None):
#         self._items = sorted(initial) if initial is not None else []
#
#     # Required sequence methods
#     def __getitem__(self, index):
#         return self._items[index]
#
#     def __len__(self):
#         return len(self._items)
#
#     # Method for adding an item in the right location
#     def add(self, item):
#         bisect.insort(self._items, item)
#
#
# items = SortedItems([5, 1, 3])
# print(list(items))
# print(items[0], items[-1])
# items.add(2)
# print(list(items))

# 属性代理访问，你想将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一个替代方法或者实现代理模式。

# class A:
#     def spam(self, x):
#         pass
#
#     def foo(self):
#         pass
#
#
# class B1:
#     """简单代理"""
#
#     def __init__(self):
#         self._a = A()
#
#     def spam(self, x):
#         return self._a.spam(x)
#
#     def foo(self):
#         return self._a.foo()
#
#     def bar(self):
#         pass
#
#
# # 若是大量方法需要代理 可使用__getattr__()方法
# 当实现代理模式时，还有些细节需要注意。 首先，__getattr__() 实际是一个后备方法，只有在属性不存在时才会调用。
# 因此，如果代理类实例本身有这个属性的话，那么不会触发这个方法的。 另外，__setattr__() 和 __delattr__() 需要额外的魔法来区分代理实例和被代理实例 _obj 的属性
# class B2:
#     def __init__(self):
#         self._a = A()
#
#     def bar(self):
#         print('b2 bar func')
#
#     def __getattr__(self, name):
#         return getattr(self._a, name)
#
# b=B2()
# b.bar()
# b.spam(42)
# class Proxy:
#     def __init__(self, obj):
#         self._obj = obj
#
#     def __getattr__(self, name):
#         print('getattr:', name)
#         return getattr(self._obj, name)
#
#     def __setattr__(self, name, value):
#         if name.startwith('_'):
#             super().__setattr__(name, value)
#         else:
#             print('setattr:', name, value)
#             setattr(self._obj, name, value)
#
#     def __delattr__(self, name):
#         if name.startwith('_'):
#             super().__delattr__(name)
#
#         else:
#             print('delattr:', name)
#             delattr(self._obj, name)
#
#
# class Spam:
#     def __init__(self, x):
#         self.x = x
#
#     def bar(self, y):
#         print('spam.bar', self.x, y)
#
#
# s = Spam(2)
# print(s.bar(3))
#
# p = Proxy(s)
# print(p.x)  # Outputs 2
# p.bar(3)  # Outputs "Spam.bar: 2 3"
# p.x = 37  # Changes s.x to 37

# 在类中定义多个构造器
# import time
#
#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def today(cls):
#         """类方法的一个主要用途就是定义多个构造器。它接受一个 class 作为第一个参数(cls)。
#         你应该注意到了这个类被用来创建并返回最终的实例。在继承时也能工作的很好："""
#         t = time.localtime()
#         return cls(t.tm_year, t.tm_mon, t.tm_mday)
#
#     def get_value(self):
#         return self.year,self.month,self.day
#
# a = Date(2012, 12, 21) # Primary
# print(type(a),a.__dict__,a.get_value())
# b = Date.today() # Alternate
# print(type(b),b.__dict__,b.get_value())
#
# # 创建一个实例绕过__init__()
# from time import localtime
#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def today(cls):
#         d = cls.__new__(cls)
#         t = localtime()
#         d.year = t.tm_year
#         d.month = t.tm_mon
#         d.day = t.tm_mday
#         return d

# 实现一个状态机或是在不同状态下执行操作的对象，但又不想在代码中出现太多的条件判断

# class Connection:
#     """普通方案，好多个判断语句，效率低下~~"""
#
#     def __init__(self):
#         self.state = 'CLOSED'
#
#     def read(self):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not open')
#         print('reading')
#
#     def write(self, data):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not open')
#         print('writing')
#
#     def open(self):
#         if self.state == 'OPEN':
#             raise RuntimeError('Already open')
#         self.state = 'OPEN'
#
#     def close(self):
#         if self.state == 'CLOSED':
#             raise RuntimeError('Already closed')
#         self.state = 'CLOSED'
#
#
# # 上述代码条件判断多 代码复杂 效率低
# # Connection state base class
# class ConnectionState:
#     @staticmethod
#     def read(conn):
#         raise NotImplementedError()
#
#     @staticmethod
#     def write(conn, data):
#         raise NotImplementedError()
#
#     @staticmethod
#     def open(conn):
#         raise NotImplementedError()
#
#     @staticmethod
#     def close(conn):
#         raise NotImplementedError()
#
# # Implementation of different states
# class ClosedConnectionState(ConnectionState):
#     @staticmethod
#     def read(conn):
#         raise RuntimeError('Not open')
#
#     @staticmethod
#     def write(conn, data):
#         raise RuntimeError('Not open')
#
#     @staticmethod
#     def open(conn):
#         conn.new_state(OpenConnectionState)
#
#     @staticmethod
#     def close(conn):
#         raise RuntimeError('Already closed')
#
#
# class OpenConnectionState(ConnectionState):
#     @staticmethod
#     def read(conn):
#         print('reading')
#
#     @staticmethod
#     def write(conn, data):
#         print('writing')
#
#     @staticmethod
#     def open(conn):
#         raise RuntimeError('Already open')
#
#     @staticmethod
#     def close(conn):
#         conn.new_state(ClosedConnectionState)
#
# class Connection1:
#     def __init__(self):
#         self.new_state(ClosedConnectionState)
#
#     def new_state(self, newstate):
#         self._state = newstate
#
#     def read(self):
#         return self._state.read(self)
#
#     def write(self, data):
#         return self._state.write(self, data)
#
#     def open(self):
#         return self._state.open(self)
#
#     def close(self):
#         return self._state.close(self)
#
# c = Connection1()
# print(c._state)
# print(c.read())
# print(c.open())

# 通过字符串形式，调用某个对象的对应方法
# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Point({!r:},{!r:})'.format(self.x, self.y)
#
#     def distance(self, x, y):
#         return math.hypot(self.x - x, self.y - y)
#
#
# p = Point(2, 3)
# d = getattr(p, 'distance')(0, 0)
# print(d,'\n')
# # 或者
# import operator
# print(operator.methodcaller('distance',0,0)(p))

# 你要处理由大量不同类型的对象组成的复杂数据结构，每一个对象都需要进行不同的处理。
# 比如，遍历一个树形结构，然后根据每个节点的相应状态执行不同的操作。
# 这里遇到的问题在编程领域中是很普遍的，有时候会构建一个由大量不同对象组成的数据结构。
# class Node:
#     pass
#
#
# class UnaryOperator(Node):
#     def __init__(self, operand):
#         self.operand = operand
#
#
# class BinaryOperator(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#
# class Add(BinaryOperator):
#     pass
#
#
# class Sub(BinaryOperator):
#     pass
#
#
# class Mul(BinaryOperator):
#     pass
#
#
# class Div(BinaryOperator):
#     pass
#
#
# class Negate(UnaryOperator):
#     pass
#
#
# class Number(Node):
#     def __init__(self, value):
#         self.value = value
#
#
# t1 = Sub(Number(3), Number(4))  # 嵌套的数据结构
# t2 = Mul(Number(2), t1)
# t3 = Div(t2, Number(5))
# t4 = Add(Number(1), t3)
#
#
# # 这样做的问题是对于每个表达式，每次都要重新定义一遍，有没有一种更通用的方式让它支持所有的数字和操作符呢。
# class NodeVisitor:
#     def visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         print('meth--',meth)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#
#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
#
# class Evaluator(NodeVisitor):
#     def visit_Number(self,node):
#         return node.value
#
#     def visit_Add(self,node):
#         return self.visit(node.left) + self.visit(node.right)  # 或者 yield (yield node.left) + (yield node.right)
#
#     def visit_Sub(self, node):
#         return self.visit(node.left) - self.visit(node.right)
#     def visit_Mul(self, node):
#         return self.visit(node.left) * self.visit(node.right)
#     def visit_Div(self, node):
#         return self.visit(node.left) / self.visit(node.right)
#     def visit_Negate(self, node):
#         return -node.operand
#
# e = Evaluator()
# print(t4,type(t4),t4.__dict__)
# print(e.visit(t4))

# 不递归的访问者模式
# 你使用访问者模式遍历一个很深的嵌套树形数据结构，并且因为超过嵌套层级限制而失败。 你想消除递归，并同时保持访问者编程模式。
# 通过巧妙的使用生成器可以在树遍历或搜索算法中消除递归。

# import types
#
# class Node:
#     pass
#
# class NodeVisitor:
#     def visit(self, node):
#         stack = [node]
#         last_result = None
#         while stack:
#             try:
#                 last = stack[-1]
#                 if isinstance(last, types.GeneratorType):
#                     stack.append(last.send(last_result))
#                     last_result = None
#                 elif isinstance(last, Node):
#                     stack.append(self._visit(stack.pop()))
#                 else:
#                     last_result = stack.pop()
#             except StopIteration:
#                 stack.pop()
#
#         return last_result
#
#     def _visit(self,node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, Node)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#
#     def generic_visit(self,node):
#         raise  RuntimeError('No {} method'.format('visit_' + type(node).__name__))

# import weakref
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self._parent = None
#         self.children = []
#
#     def __repr__(self):
#         return 'Node({!r:})'.format(self.value)
#
#     # property that manages the parent as a weak-reference
#     @property
#     def parent(self):
#         return None if self._parent is None else self._parent()
#
#     @parent.setter
#     def parent(self, node):
#         self._parent = weakref.ref(node)
#
#     def add_child(self, child):
#         self.children.append(child)
#         child.parent = self
#
# root = Node('parent')
# c1 = Node('child')
# root.add_child(c1)
# print(c1.parent)
# del root
# print("del--",c1.parent)
#
# import gc
# print(gc.collect())
#
