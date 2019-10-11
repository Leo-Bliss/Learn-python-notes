'''
Today is August 2,2019
Life is not only in front of you,
but also in poetry and afar. 
'''

#list
'''
#列表和字符串

#相同点
1.索引（[]运算符）
2.切片（[:]）
3.拼接（+），和重复（*）
4.成员运算符（in）
5.长度（len（））
6.循环（for）

#不同点

1.使用[]生成，元素之间用逗号分隔
2.可以包含多种类型的对象，字符串只能是字符
3.列表内容可变，字符串不可变
'''
a = [1] * 3
print(a)
b = [2] * 2
print(a+b)
my_list = [13,'aad',12.3,98,456,123]
print(my_list)
print(my_list[1])
#更改
my_list[0] = 12
#索引
print(my_list[0])
#切片
print(my_list[0:-2])
#追加：

#尾部追加一个元素
my_list.append('asa')
print(my_list)
#尾部追加一个列表
my_list.extend(['abcd','456'])
print(my_list)

#插入my_list.insert(pos,value)
my_list.insert(1,123)
print(my_list)

#删除元素：

#尾部弹出
#默认最后一个
my_list.pop()
print(my_list)
#也可以指定pos
my_list.pop(2)
print(my_list)
#移除第一个值为value的元素
my_list.remove(123)
print(my_list)

#排序
my_list2 = [3,1,2]
my_list2.sort()
print(my_list2)
#反转
my_list.reverse()
print(my_list)
'''
#求多个数平均值

nums = []
for i in range(5):
      nums.append(float(input()))
s = 0
for num in nums:
      s += num
avg = s / 5
print(avg)
'''
#内建函数：sum,max,min
c = [6,7,5,2,4,3,1]
print(sum(c)/len(c))
print(max(c))
print(min(c))
