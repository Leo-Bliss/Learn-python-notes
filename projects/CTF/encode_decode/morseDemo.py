#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/5 0005 9:42
#@Author  :    tb_youth
#@FileName:    morseDemo.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

class Morse(object):
    key_list1 = ['01', '1000', '1010', '100', '0', '0010',
                '110', '0000', '00', '0111', '101', '0100',
                '11', '10', '111', '0110', '1101', '010',
                '000', '1', '001', '0001', '011', '1001',
                '1011', '1100', '01111', '00111', '00011',
                '00001', '00000', '10000', '11000', '11100',
                '11110', '11111', '001100', '10010', '101101',
                '100001', '010101', '110011', '011010', '111000',
                '101010', '10001', '011110', '101011', '001101',
                '010010', '10110', '1111011', '1111101']

    value_list = ['A', 'B', 'C', 'D', 'E','F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                  'W', 'X', 'Y', 'Z', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9', '0', '?', '/',
                  '()', '-', '.', ',', '@', ':', ':',
                  '=', "'", '!', '_', '"', '(', '{', '}']

    def __init__(self):
        self.key_list2 = [item.replace('0','.').replace('1','-') for item in self.key_list1]
        self.encode_dict = dict(zip(self.value_list,self.key_list2))
        self.decode_dict = dict(zip(self.key_list2,self.value_list))

    def decode(self,string):
        word_list = string.split()
        res1 = ''.join([self.decode_dict.get(word.strip()) for word in word_list])
        res2 = res1.lower()
        print('Decode reslut following:')
        print('Upper result:',res1)
        print('Lower result:',res2)
        return res1,res2

    def encode(self,string):
        res1 = ' '.join([self.encode_dict.get(item) for item in string])
        res2 = res1.replace('.','0').replace('-','1')
        print('Encode reslut following:')
        print('Std result:',res1)
        print('01 result:',res2)
        return res1,res2


if __name__=='__main__':
    s = '-... -.- -.-. - ..-. -- .. ... -.-.'.strip()
    m = Morse()
    m.decode(s)
    print(m.encode('BKCTFMISC')[0]==s)
    ss = '0010 0100 01 110 1111011 11 11111 010 000 0 001101 1010 111 100 0 001101 01111 000 001101 00 10 1 0 010 0 000 1 01111 10 11110 101011 1111101'
    ss = ss.replace('0','.').replace('1','-')
    print(ss)
    m.decode(ss)



