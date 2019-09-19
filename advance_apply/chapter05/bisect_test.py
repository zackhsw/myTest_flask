import bisect
from collections import deque

# 用来处理已排序的序列，用来维持已排序的序列，升序
# 二分查找

inter_list = []  # inter_list=deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)  # [1, 2, 3, 5, 6] 输出了已排序的序列，这个方法排序效率高

inter_left = bisect.bisect_left(inter_list, 3.0)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这时3存在于列表中，返回左侧位置
print(inter_left)
print(inter_list)
