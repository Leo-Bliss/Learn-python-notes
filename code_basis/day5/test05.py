'''
Today is July,30,2019
Keep a pastive and healthy mindset!

'''

'''
#局部变量和全局变量
x = 1 #全局
def f1():
      x = 2 #局部
      print(x)
f1()
print(x)
print("-------------------")
y = 1
def f2():
      global y #声明此时y和外面的全局变量为同一变量
      y += 1
      print(y)
f2()
print(y)
'''
'''
#判断回文素数

import math
#回文
def is_palin(num):
      tmp = num
      s = 0
      while tmp:
            s += s*10 + tmp % 10
            tmp //= 10
      return s == num
#素数

def is_prime(num):
      if(num <= 3):
           if(num == 2 or num == 3):
                  return True
           else:
                  return False
      else:
            for i in range(2,int(math.sqrt(num))+1):
                  if num % i == 0:
                        return False
            return True
if __name__ =='__main__':
      num = int(input())
      if(is_palin(num) and is_prime(num)):
            print(num, "是回文素数")
      else:
            print(num,"不是回文素数")
'''

# n!递归程序
def p(n):
      if n == 0 or n == 1:
            return 1
      else:
            return n*p(n-1)
      
# Fibonacci序列递归程序
def fib(n):
      if n == 1 or n == 2:
            return 1
      else:
            return fib(n-1) + fib(n-2)
      
if __name__ =='__main__':
      n = int(input())
      #print(p(n))
      print(fib(n))
