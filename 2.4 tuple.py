"""
2.4 基本数据类型 -- tuple(元组)
"""

## 用法与list基本一致，不同的是
# tuple用()， list用[]
# tuple不可修改序列元素， list可修改序列元素

# 创建元组
tuple1 = (1, "a", "ss", 1+2j)
print(id(tuple1))
tuple1 = 2, "b", "ss1", 2+2j ## 不需要括号也可以
print(id(tuple1))

a = (50)
print(type(a)) # 不加逗号，为整型
a = (50,)
print(type(a)) # 加上逗号，为元组