
'''
Taday is July 27,2019.
Keep kindness in your heart.
'''
'''
def transform_F_C(F):
      C = 5 * (F - 32) / 9
      return C
if __name__=='__main__':
      F = float(input("请输入华氏度:"))
      print("转化为摄氏度为:",transform_F_C(F))
''' 

'''
查看模块有哪些方法：
dir(module)

查看该模块方法如何使用：
help(module.way)
'''
'''
import math

if __name__=='__main__':
      #print(dir(math))
      #print(help(math.sqrt))
      x = math.acos(-1.0) #PI
      print(x)
      
     
'''

#判断闰年
def judge_leap_year(y):
      return(y % 100 == 0 and y % 4 != 0) or (y % 400 == 0)

if __name__=='__main__':
   
      #多组输入，遇到异常结束，比如EOF
      while True:
            try:
              y = int(input())
              print(judge_leap_year(y))
            except:
                  break






