'''
2. 基本数据类型
'''

## 变量赋值
a = 1; b = 1.0; c = "字符串"
print(a, b, c, sep=", ")

## 多个变量赋值
a = b = c = "ok"
print(a, b, c)

a, b, c = 1, 1.0, "ok"
print(a, b, c)

## 标准数据类型
## 不可变数据类型 Number(数字)，String(字符串)，Tuple(元组)
## 可变数据类型   List(列表)，Set(集合)，Dictionary(字典)

#  Number (python3 支持int, float, bool, complex（复数）)
a, b, c, d, e = 1, 1.0, True, 2+2j, complex(2, 3) #复数：https://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365?fr=aladdin
print(type(a), type(b), type(c), type(d), type(e))
print(isinstance(a, int), isinstance(b, float), isinstance(c, bool), isinstance(d, complex), isinstance(e, complex))

# String
a = "字符串"
print(type(a), isinstance(a, str))

# Tuple: (value1, value2, ...)
_tuple = ("a", 1, 1.0, False, 2+3j)
print(type(_tuple), isinstance(_tuple, tuple))

# List: [value1, value2, ...]
_list = ["a", 1, 1.0, False, 2+3j]
print(type(_list), isinstance(_list, list))

# Set: {value1, value2, ...}
_set = {"a", 1, 1.0, False, 2+3j}
print(type(_set), isinstance(_set, set))

# Dictionary: {key1 : value1, key2 : value2, ...} 键的类型须为Number或String，值的类型为任意类型
_dict = {"a":"a", "b": 1, 1 : "a", 1.0 : 1, False : 0, 2+3j : 1, 2 : _set}
print(type(_dict), isinstance(_dict, dict))