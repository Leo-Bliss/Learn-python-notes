'''
Today is July,31,2019

Always love life!

'''


#字符串(String)

#表示：
'''
单引号,双引号括起来,
如果字符串内部有单引号，则外部应用双引号（或者内部用转义字符'\'）,
如果内部有双引号，处理方式与上面同理
除此之外，还可以用三引号（保留字符串中全部格式信息，多行注释用的是三引号）
'''
t = "I'm a student."
print(t)
s = "hello world"

#len(s)：字符串长度
print(len(s))

#字符串拼接：+
h = 'hello '
g = "github!"
print(h+g)

#字符串重复：*
name = 'Bob'
print(name*3)

#成员运算：in
#如果一个字符串是另一个字符串的子串返回True,否则返回False,大小写铭感

s2 = 'hello'
print(s2 in s)

#练习:

#编写一个函数统计字符串中元音个数

def vowels_count(s):
      count = 0
      for c in s:
            if c in "AEIOUaeiou":
                  count += 1
      return count
print(vowels_count("hello github!"))

#字符串索引：[start:finish],
#start默认为第一个字符的位置，finish默认为字符串最后一个字符的下一个位置

my_str = "You should be confident!"
print(my_str[11:15])
print(my_str[11:])
print(my_str[:6])
#索引可以有三个参数：[start:finish:countBy],第三参数countBy为步长
print(my_str[0:16:2])
#原串的逆序
print(my_str[::-1])
#字符串不可变，不能通过下标值改变某个字符
'''
要通过原串获得一个有改变的新串，
我们可以通过切片来改变,
原串要变则将新串赋值个原串
'''
s3 = 'hello world'
s4 = s3[:4]+'a' + s3[4:]
print(s4)

#replace方法my_str.replace(old,new)：
my_str2 = 'hello world'
print(my_str2.replace('o','a'))
#replace方法生成一个新串，原字符串不变（字符串不可变）
print(my_str2)

#find方法，my_str.find(t),返回查找到的第一个次出现的下标位置
print(my_str2.find('l'))

#split方法，my_str.split(t),通过字符(串)t分割成多个串，默认为空格
print(my_str2.split())
print(my_str2.split('ll'))









