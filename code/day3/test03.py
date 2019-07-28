'''
Taday is July,28,2019
You should believe in youself and insist on doing what you want to do.
'''

#求常数e
# e = 1 + 1/(1!) + 1/(2!) + 1/(3!)+...+1/(i!)

#way1
s = 1
tmp = 1
for i in range(1,100):
      tmp *= i
      s += 1/tmp
print(s)

#way2
import math
s = 1
for i in range(1,100):
      s += 1/(math.factorial(i))
print(s)

#求常数PI(圆周率)
#PI = 4*(1-1/3+1/5-1/7+1/9-1/11+..+(-1)^(i+1)/(2*i-1))
PI = 0
for i in range(1,10000):
      if(i&1):
            PI += 1 / (2 * i - 1)
      else:
            PI -= 1 / (2 * i - 1)
print(4*PI)
'''
for i in range(2,6):
      print(i,end = ' ')
print(' ')
for i in range(2,15,3):
      print(i,end = ' ')
print(' ')   
for i in range(15,2,-1):
      print(i,end = ' ')
'''
'''
range 函数：
range(start,stop[,step])
例子：
range(2,6) -->2 3 4 5
range(2,15,3) -->2 5 8 11 14
range(15,2,-1) -->15 14 13 12 11 10 9 8 7 6 5 4 3

'''

'''
#计算一元二次方程的解
# ax^2 + bx + c = 0
import math
a = float(input())
b = float(input())
c = float(input())
# x1 = (-b + sqrt((b^2-4*a*c)))/(2*a),x2 = (-b - sqrt((b^2-4*a*c)))/(2*a)
dalta = b ** 2 - 4 * a * c
if dalta < 0:
      print("No answer")
elif dalta == 0:
      x = -b / (2 * a)
      print(x)
else:
      root = math.sqrt(dalta)
      x1 = (-b + root) / (2 * a)
      x2 = (-b - root) / (2 * a)
      print(x1,x2)
'''
      
