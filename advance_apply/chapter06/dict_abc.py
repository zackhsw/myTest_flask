from collections.abc import Mapping,MutableMapping
# dict 属于mapping类型
# dd = dict()
dd = {}
print(isinstance(dd,MutableMapping))  # 实际上MutableMapping将dict注册了起来