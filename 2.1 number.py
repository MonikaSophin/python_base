import math;
import random;
"""
2.1 基本数据类型 -- Number(数字)
"""

## 赋值与删除
a = 1
print(a)
del a

## 数字类型转换
a = 1.0
print(a)
a = int(a)
print(a)
a = float(a)
print(a)
a = complex(a)
print(a)

## 数字运算
a, b = 3 , 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) #取整余
print(a ** b) #幂乘

## 数字常量
print("pi =", math.pi)
print("e =", math.e)

## 数学函数
print("abs(-10) =", abs(-10)) #绝对值
print("max(1, 2, 5) =", max(1, 2, 5))
print("min(1, 2, 5) =", min(1, 2, 5))
print("round(1.5555, 2) =", round(1.5555, 2))
print("math.fabs(-10) =", math.fabs(-10)) #绝对值
print("math.ceil(4.1) =", math.ceil(4.1)) #向上取整
print("math.floor(4.1) =", math.floor(4.1)) #向下取整
x = 1; print("math.exp(1) =", math.exp(x)) #e的x次方
print("math.log(math.e**100) =", math.log(math.e**100)) #loge 默认基数常量e
print("math.log(4, 2) =", math.log(4, 2)) #log2
print("math.log2(4) =", math.log2(4)) #log2
print("math.log10(100) =", math.log10(100)) #log10
print("math.modf(2.5) =", math.modf(2.5))
print("math.pow(2, 3) =", math.pow(2, 3)) #次幂
print("math.sqrt(4) =", math.sqrt(4)) #平方根
#三角函数等
print(math.sin(math.pi/6)) # 以弧度为单位，求其正弦值 180°（角度） = π（弧度）
print(math.degrees(math.pi)) # 弧度转为角度
print(math.radians(180)) # 角度转为弧度

## 随机数函数
_list = range(0, 10)
print(random.choice(_list)) # 从序列中随机取得一个元素
print(random.randrange(0, 10, 2)) # 开始为0，结束为10，步长为2的集合中随机取一个元素
print(random.random()) # 随机生成下一个实数，它在[0,1)范围内。
_list = [1, 2, 3, 5, 8]; random.shuffle(_list); print(_list) # 将列表随机排序，然后返回None。
print(random.uniform(7, 9)) # 随机生成下一个实数，它在[x,y]范围内。
