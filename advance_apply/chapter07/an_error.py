def add(a, b):
    a += b  # + 和 += 是不一样的
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    com = Company("xx",["sa","sb"])
    com.add("sc")
    com.remove("sa")
    print(com.staffs)

    com1 = Company("yy")
    com1.add("aa")
    print(com1.staffs)

    com2 = Company("zz")
    com2.add("bb")
    print(com2.staffs)  # ['aa', 'bb'] 居然包含'aa'
    # 因为没有传递staffs 另外staffs=[]是可变的，使得com1与com2共用了同一个list [], 建议传参不要用list 要留意list是可能被修改
    # 这也是查找问题的一个点
    print(com1.staffs is com2.staffs) # True


    # a =1
    # b=2
    # c = add(a,b)
    # print(c)
    # print(a,b)

    # a = [1, 2]
    # b = [3, 4]
    # c = add(a, b)
    # print(c)
    # print(a, b)
    #
    # a = (1, 2)
    # b = (3, 4)
    # c = add(a, b)
    # print(c)
    # print(a, b)
