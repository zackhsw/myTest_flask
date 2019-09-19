import numbers


class Group:
    """支持切片功能"""

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()  # 这里利用了list的reverse实现反转

    def __getitem__(self, item):
        """是实现切片的关键
        item是什么？item索引的类型
        """
        cls = type(self)
        if isinstance(item,slice):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])
        # 这样实现返回的依然是Group类型 而不是下面的reture 返回的slice （即list）
        # return self.staffs[item]

    def __len__(self):
        """实现len()"""
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["aa", "bb","cc", "dd"]
group = Group(company_name="mmm", group_name="user", staffs=staffs)
print(group[::])  # ['aa', 'bb']  对于# return self.staffs[item]
print(group[2])  #
print(len(group))  #
print(reversed(group))
if "aa" in group:
    print("yes")
for user in group:
    print(user)
