'''
Today is July,29,2019
Dont't be angry, don't be sad.
Everything will be Ok.
'''

'''
#打印9*9乘法表
for i in range(1,10):
      for j in range(1,10):
            #print("%d * %d = %d"%(i,j,i*j))
            print (format(i*j,'3d'),end=' ')
      print("")

'''
'''
#二分求平方根
x = float(input())
if x < 0:
      print("No solution")
elif x == 0:
      print(0)
else:
      low = 0.0
      high = x
      if x > 0 and x < 1.0:
                 high = 1.0
      mid = (low + high)/2.0
      while(abs(mid**2-x)>1e-5):
            if(mid**2 > x):
                  high = mid
            else:
                  low = mid
            mid = (low + high)/2.0
      print(mid)
'''
#判断素数
import math
def judge_prime(num):
      if(num <= 3):
            if num == 2 or num == 3:
                  return True
            else:
                  return False
      for i in  range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                  return False
      return True

#判断回文
def judge(num):
      tmp = num
      s = 0
      while num:
            s = s * 10 + num % 10
            num //= 10
      return tmp == s

if __name__=='__main__':
      while True:
            try:
                  n = int(input())
                  #print(judge_prime(n))
                  print(judge(n))
            except:
                  break
            
            
