'''
Today is August 7,2019.
If there were less sympathy in the word,
there would be less trouble in the word.
'''


#元组tuple
'''
元组即不可变得列表：
1.除会改变的方法不可用外，其他方法均适用
***
索引，切片，len（）等可用，
但是append,extend,del等不可用
***

'''
#元组的创建
'''
way1（ ','隔开）: x,y 
way2（ ','隔开再加'()'）: (x,y)
'''
my_tuple = 1,2,True
print(my_tuple)
my_tuple = (1,3,False)
print(my_tuple)

#用元组，是为了元素不可修改

#元组赋值
a,b = 1,2
print((a,b))

#交换两个值
a,b = b,a
print((a,b))

#切分字符串

name,domain = '2323@qq.com'.split('@')
print((name,domain))
#函数可以返回一个元组
def get_max_min(tpl):
      maxx = minx = tpl[0]
      for e in tpl:
            if e > maxx:
                  maxx = e
            elif e < minx:
                  minx = e
      return maxx,minx
my_tuple = (1,3,5,6,9,4,3)
print(get_max_min(my_tuple))

#DSU模式(Decorate装饰，Sort排序，Undecorate反装饰)

#对单词排序，根据单词长度排序
def word_sort(words):
      lst = []
      for word in  words:
            lst.append((len(word),word))
      lst.sort(reverse = True)
      res = []
      for length,word in lst:
            res.append(word)
      print(res)
words = ['sasa','ddfd','sd','tdfde','tssfssd']
word_sort(words)
#直接用lambda表达式
print(words)
words.sort(key = lambda x:len(x),reverse = True)
print(words)



