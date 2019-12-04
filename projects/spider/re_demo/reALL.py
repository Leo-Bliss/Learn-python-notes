#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/23 0023 14:48
#@Author  :    tb_youth
#@FileName:    reALL.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


'''
正则表达式：用于检索，替换字符串
常用的方法：
#检索
match：从头匹配1个
search：整个串匹配1个
findall：匹配所有，返回列表
finditer：匹配结果返回一个迭代器
complie
#替换
sub
'''
import re
# text = '454545fgfgfAAA@163.com$'
# pattern = '\w+@\w+\.com'
# res_match = re.match(pattern,text)
# print(res_match.group(0))
# tel = '15552986666'
# pattern_tel = '\d{11}'
# print(re.match(pattern_tel,tel))
# {,} : 0 - inf ---> *
# + = {1,}
# * = {0,}
# ? = {0,1}

# []代表中括号里的内容可以被匹配
#[123] = (1|2|3)
#\d = [0123456789] = [0-9]
#[a-z]
#[A-Z]
#[a-zA-Z0-9_]
# #email: '[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-z]+'
# line = 'abc|123|abc'
# pattern_or = '123|abc'
# print(re.match(pattern_or,line))
# ^除了作为开始还有非，[^123]：非123
#\s 空白字符，\S非空白字符


'''
complie 的作用：能够生成一个类，这个类用于匹配数据，
能够提高性能（减少频繁创建类与销毁类）。
常用于循环匹配内容的时候
'''
pattern = '\w+@\w+\.com'
line = '123456@qq.com'
res_match = re.search(pattern,line)
print(res_match)
#下面两行等价于上面的一行
pat = re.compile(pattern)
res_match = pat.search(line)
print(res_match)

#sub
line = 'I am student'
pattern = '[a-zA-Z]+'
print(re.sub(pattern,'666',line)) #666 666 666


#w3lib.html 中remove_tags方法
# 去除html标签