# a = dict()
a = {"aaa":{"inner_aaa":"inner_value"}}
# a.clear()

# copy返回浅拷贝
# new_dict = a.copy()
# new_dict["aaa"]["inner_aaa"] = "cccc"  # a 字典也会受到改变 inner_aaa键值受影响

# 深拷贝
# import copy
# new_dict = copy.deepcopy(a)
# new_dict["aaa"]["inner_aaa"] = "cccc"

# formkeys
new_list = ["n1","n2"]
# new_list 各元素做键
new_dict = dict.fromkeys(new_list,{"k1":"v1"})  # {'n1': {'k1': 'v1'}, 'n2': {'k1': 'v1'}}

value = new_dict.get("n1",{})  # {'k1': 'v1'}

default_value = new_dict.setdefault("default_k","default_v") # 没有default_k 设置default_v
# print(default_value)
# print(new_dict,value,default_value)
# {'n1': {'k1': 'v1'}, 'n2': {'k1': 'v1'}, 'default_k': 'default_v'} {'k1': 'v1'} default_v

new_dict.update((("uu","nn"),))
# new_dict.update({"uu":"nn"})
print(new_dict)