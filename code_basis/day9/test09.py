'''
Today is August 5,2019
The truth is a beautiful and terrible
thing,and should therefore be treated
with great caution.
'''

#列表复制
a = [1,2,3]
#只是将b指向了a列表的地址，改变b会改变a
b = a
b[1] = 4
print('b : ',b)
print('a : ',a)
#得到a列表的一个拷贝（即新列表），改变c不影响a
c = a[:]
c[2] = 5
print('a : ',a)
print('c : ',c)


#交换列表中元素的值
def my_swap(lst,x,y):
      tmp = lst[x]
      lst[x] = lst[y]
      lst[y] = tmp
my_list = [1,5,2,4,6,3,8]
print(my_list)
my_swap(my_list,1,3)
print(my_list)

#查找列表元素，并返回下标

'''
第一个等于目标值的下标
找不到返回-1

'''

def my_search(lst,value):
      n = len(lst)
      for i in range(n):
            if lst[i] == value:
                  return i
      return -1
my_list2 = [1,2,3,2,5,6,3,4]
print('my_list : ',my_list2)
print('value = 2,resIndex = ',my_search(my_list2,2))
print('value = 9,resIndex = ',my_search(my_list2,9))

#index方法，my_list.index(value),找不到value会抛出异常
print('list中index方法search,value = 2,resIndex = ',my_list2.index(2))

#binary_search,二分查找

def binary_search(lst,value):
      low = 0
      high = len(lst)-1
      while(low <= high):
            mid = (low + high)>>1
            if(lst[mid] < value):
                  low = mid + 1
            elif(lst[mid] > value):
                  high = mid - 1
            else:
                  return mid
      return -1
my_list3 = [1,4,5,7,8,9]
print(binary_search(my_list3,5))



