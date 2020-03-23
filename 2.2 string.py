"""
2.2 基本数据类型 -- String(字符串)
"""

## 字符串运算符
str1 = "hello world!"
print(str1)
# + 字符串拼接
print(str1 + " 你好")
# * 重复输出字符串
print(str1 * 3)
# [] 通过索引访问字符串
print("str1[1] =", str1[1])
# [:] 通过左闭右开区间截取字符串
print("str1[1:4] =", str1[1:4])
# in 成员运算符（不区分大小写） - 如果字符串中包含给定的字符返回 True
print("h in str1", "h" in str1)
# not in 成员运算符（不区分大小写） - 如果字符串中不包含给定的字符返回 True
print("h not in str1", "h" not in str1)
# r/R 按照原义输出，不转义任意转义字符
print(r"\n"); print(R"\n")

## 字符串格式化
print("%s 打了 %s %d 拳" %("小明", "小红", 1))

## 三引号
more_str = """多行字符串
可以使用制表符(\t)和换行符(\n) 
"""
print(more_str)

## f-string [python3.6之后格式化字符串的语法]
dict1 = {"name":"小王", "age":28}
s1 = "姓名:" f'{dict1["name"]},' + "年龄:" f'{dict1["age"]}'
print(s1)
x = 1
print(f'{x + 1}') #python3.6
print(f"{x + 1 = }") #python3.8 用=拼接表达式和结果

