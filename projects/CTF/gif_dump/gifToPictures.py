#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/5 0005 0:46
#@Author  :    tb_youth
#@FileName:    gifToPictures.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
gif图片分离成图片
'''

from PIL import Image
import os
# from projects.CTF.QR_code import QRCode

def gif_to_pictures(gif_file):
  image = Image.open(gif_file)
  dir = gif_file.split('/')[-1].strip('.gif')
  # print(dir)
  os.mkdir(dir)
  try:
    while True:
      current = image.tell()
      image.save('{0}/{1}.png'.format(dir,current))
      image.seek(current+1)
  except Exception as e:
    pass

if __name__=='__main__':
  gif_file = r'./masterGo.gif'
  gif_to_pictures(gif_file)
  # qr = QRCode.QRCodeDemo()
  # res = ''
  # for i in range(18):
  #   file = './masterGo/{0}.png'.format(i)
  #   image = Image.open(file)
  #   res += qr.scan(image)
  # print(res)