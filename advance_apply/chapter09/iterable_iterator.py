from collections.abc import Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # def __getitem__(self, item):  # item 为索引值
    #     return self.employee[item]

    def __iter__(self):
        return MyIterator(self.employee)


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['aa', 'bb', 'cc'])

    my_itor = iter(company)
    while True:
        try:
            next(my_itor)
        except StopIteration:
            pass

    # for item in company:
    #     print(item)
