#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   原始数据结构.py
@Time    :   2020/03/16 22:22:21
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib

'''
原始数据结构
'''

# Integers：您可以使用Integers表示数字数据，具体地说，可以使用从负无穷大到无穷大的整数
number_1 = 1
number_2 = 2
number_3 = 3
print(number_1,number_1+number_2,number_1*number_2)
print(number_3/number_1,number_3%number_1)

# Float:“Float”代表“浮点数”。 您可以将它用于有理数，通常以十进制数字结尾，例如1.11或3.14。计算同Integers.
print(3/2)#整形相除得浮点
print(3//2)#整除

# String： String是字母，单词或其他字符的集合。 在Python中，您可以通过在一对单引号或双引号中包含一系列字符来创建字符串。
x = 'Cake'
y = 'Cookie'
x + ' & ' + y #结果:'Cake & Cookie'

# Repeat
x * 2 #结果：'CakeCake'

# split
z1 = x[2:] 
print(z1)
z2 = y[0] + y[1] 
print(z2)
# 结果 ke Co

# 内置辅助方法

# 大写首字母
str.capitalize("cookie")

# 以字符为单位检索字符串的长度,空格同时计数
str1 = "Cake 4 U"
str2 = "404"
print(len(str1))

# 检查字符串是否数字
str1 = "Cake 4 U"
str2 = "404"
str1.isdigit()
# False
str2.isdigit()
# True

# 替换
str1 = "Cake 4 U"
str2 = "404"
str1.replace('4 U', str2)
# 'Cake 404'

# 查找子字符串
str1 = 'cookie'
str2 = 'cook'
str1.find(str2)
# 0
str1 = 'I got you a cookie'
str2 = 'cook'
str1.find(str2)
# 12

# Boolean:这种内置数据类型值为：True和False，这通常使它们可以与整数1和0互换。
x = 4
y = 2
print(x == y)
# False
print(x > y)
# True

x = 4
y = 2
z = (x==y)
if z:
    print("Cookie")
else:
    print("No Cookie")
# No Cookie

# 数据类型转化

#查看数据类型
i = 4.0
print(type(i))
# float

# 隐式数据类型转换:数据类型自动转换，不需要指定，编译器会为您处理。
# float
x = 4.0 
# integer
y = 2 
z = x/y
print(type(z))
# float

# 显式数据类型转换

x = 0
y = "The Godfather: Part "
print(str(x),float(x),bool(x))
print(str(x) + y)