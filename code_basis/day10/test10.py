'''
Today is August 6,2019.
Don't forget the things you once
owned.Treasure the things you can't
get.Don't give up the things that
belong to you and keep those lost
things in memory.
'''
'''
#select_sort
def my_swap(lst,x,y):
      temp = lst[x]
      lst[x] = lst[y]
      lst[y] = temp

def select_sort(lst):
      length = len(lst)
      for i in range(length):
            minx = lst[i]
            pos = i
            for j in range(i+1,length):
                  if lst[j] < minx:
                        minx = lst[j]
                        pos = j
            my_swap(lst,i,pos)
      for e in lst:
            print(e,end=' ')

#bubble_sort

def bubble_sort(lst):
      length = len(lst)
      for i in range(length,0,-1):
            flag = False
            for j in range(1,i):
                  if lst[j] < lst[j-1]:
                        flag = True
                        my_swap(lst,j,j-1)
            if not flag:
                  break
      for e in lst:
            print(e,end = ' ')
            
my_list = list(map(int,input().split()))
               
#select_sort(my_list)
#bubble_sort(my_list)

#sorted(my_list),有返回值，不改变原列表
a = sorted(my_list)
print(a)
print(my_list)

#my_list.sort(),没有返回值，改变原列表
my_list.sort()
print(my_list)
'''

#嵌套列表
import sys
students = []
n = int(input())
for i in range(n):
      line = sys.stdin.readline().strip()
      stu = []
      name,score = line.split()
      score = int(score)
      #print(name,score)
      stu.append(name)
      stu.append(score)
      students.append(stu)
print(students)

#求平均分
s = 0
for st in students:
      s += st[1]
print(s/n)

#列表解析
#公式： 表达式 for 变量 in 列表 if条件
my_list2 = [x**2 for x in range(1,10)]
print(my_list2)

avg = sum(x[1] for x in students)/n
print(avg)

#students列表中按成绩降序排序
def f(a):
      return a[1]
students.sort(key = f,reverse = True)
print(students)

#lambda函数

students.sort(key = lambda x:x[1],reverse = True)
print(students)

      
