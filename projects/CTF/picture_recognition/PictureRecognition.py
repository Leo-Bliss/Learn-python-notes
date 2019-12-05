#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/4 0004 19:56
#@Author  :    tb_youth
#@FileName:    PictureRecognition.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
运行报找不到：tesseract找不到的错误
解决方案：
在python site-packages/pytesseract找到
pytesseract.py，将tesseract_cmd = 'tesseract'改成自己软件安装的路径
（我装在D:/tesseract/Tesseract-OCR/tesseract.exe）
tesseract_cmd = r'D:/tesseract/Tesseract-OCR/tesseract.exe'
补充：快捷跳转：选中image_to_string，然后Ctrl+B
'''
from PIL import Image
import pytesseract

#一般的预处理
# threshold:阈值
def convert_image(image,threshold):
    #处理灰度
    image = image.convert("L")
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            pixels[x,y] = 255 if pixels[x,y] > threshold else 0
    return image

if __name__=='__main__':
    # image = Image.open('./picture/test2.jpg')
    # # image.show()
    # # image = convert_image(image,160)
    # # image.show()
    # #报错临时解决方案
    # # pytesseract.pytesseract.tesseract_cmd = r'D:/tesseract/Tesseract-OCR/tesseract.exe'
    # res = pytesseract.image_to_string(image,lang='chi_sim')
    # print(res)

    image = Image.open('./picture/1.jpg')
    res = pytesseract.image_to_string(image)
    print(res)
    #识别准确率低！！！！
    #识别不了字母'l',误将0识别为大写字母'O'

