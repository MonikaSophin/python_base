import keyword;

'''
1.python基础语法
'''

## 关键字
print(keyword.kwlist) #输出：['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(keyword.iskeyword("False")) #输出：True

## 行与缩进
condition = True
if condition:
    print("True")
else:
    print("False") #输出：True

if condition:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False") #输出：Answer \n True

if condition:
    print("Answer")
    print("True")
else:
    print("Answer")
 # print("False") #IndentationError: unindent does not match any outer indentation level

## 字符串转义与非转义
print("hello \nworld")
print(r"hello \nworld") #在字符串前面添加一个 r，表示原始字符串，不会发生转义

## 等待用户输入：
input("\n输入任意字符\n按下 enter 键后退出")

## 同一行显示多条语句
import sys; x = "hello"; sys.stdout.write(x + "\n")

## print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
print("hello world")
print("hello world", end="")
print(" xxx")

## import 与 from...import
import sys; print("path:", sys.path)
from sys import path; print("path:", path) #因为已经导入path成员，所以此处引用时不需要加sys.path