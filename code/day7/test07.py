'''
Today is August 1,2019.

Good night!
'''


'''
#判断回文非递归写法
def is_palinedrome(name):
      low = 0
      high = len(name)-1
      while(low < high):
            if(name[low] != name[high]):
                  return False
            low += 1
            high -= 1
      return True

#判断回文递归写法
def is_palinedrome_rec(name):
      if len(name) <= 1:
            return True
      else:
            if name[0] != name[-1]:
                  return False
            else:
               return is_palinedrome_rec(name[1:-1])

#字符串比较
def is_ascending(name):
      if len(name) > 0 :
            p = name[0]
      for c in name:
            if p > c:
                  return False
            p = c
      return True
      
#文件操作，处理文本
f = open('name.txt','r')
for line in f:
      #去掉字符串开始和结尾的空格回车等字符
      line = line.strip()
      #title方法:首字母大写，其他小写
      #print(line.title())
      #判断名字是否为回文
      if(is_palinedrome_rec(line)):
            print(line)
      #判断名字中字符是否升序
      if(is_ascending(line)):
            print(line)
f.close()
#f.write(str)

'''
#格式化字符串

#输出更规格的结果

print('hello {} good {}.'.format('my','friends'))

#{file name:align width.precision type}
#域名file name，对齐方式align（>:右对齐,<:左对齐）
#占用宽度width，精度.precision,type类型（比如f，e）
import math
PI = math.acos(-1.0)
print('PI is {:.4f}'.format(PI))
print('PI is {:9.5f}'.format(PI))
print('PI is {:e}'.format(PI))



            

