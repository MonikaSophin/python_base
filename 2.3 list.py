"""
2.3 基本数据类型 -- list(列表)
"""

## 查询列表元素
list1 = ["bob", "coco", 11, 22.0]
print("list1[0:4]: " , list1[0:4])
print("list1[0]: " + list1[0])

## 更新列表元素
print("update before: " , list1)
list1[2] = "xx"
print("update after: " , list1)

## 删除列表元素
print("delete before: " , list1)
del list1[0]
print("delete after: " , list1)

## python列表脚本操作符
print(len([0, 1, 2, 4]))
print(["hi"]*4)
print(2 in [0, 1, 2, 3])
for x in [0, 1, 2] : print(x, end=" ")
print()

## python列表截取与拼接
list2 = ['a', 'b', 'c', 'd']
print(list2[:])
print(list2[::])
print(list2[0:])
print(list2[:-1])
print(list2[1:])
print(list2[1])
print(list2[-3])

## 嵌套列表
a = [0, 1, 2]
b = ['a', 'b']
c = [a, b]
print(c)
print(c[0])
print(c[0][1])

## python列表函数与方法
a1 = ['a', 'c', 'z', 'd', 'a']
# 函数
print(len(a1))
print(max(a1))
print(min(a1))
print(tuple(a1)) # 转为元组
print(set(a1)) # 转为集合
print(list(a1)) # 转为列表
# 方法
print(a1.append("x"), end="   "), print(a1)
print(a1.count('a')) # 统计元素在列表出现的次数
print(a1.extend(('1', '3', '5')), end=" "), print(a1) #在列表末尾追加另一个序列
print(a1.sort(), end="  "), print(a1)
s = sorted(a1, reverse=True); print(s)