#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/21 0021 22:19
#@Author  :    tb_youth
#@FileName:    HandelPhoto.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

from removebg import RemoveBg
import os
from PIL import Image


class HandePhotosDemo(object):
    def __init__(self):
        pass

    #得到透明背景图片
    def getTransparentBackgroPicture(self,api_key=None,file=None,url=None):
        #官网申请的api_key
        rmbg = RemoveBg(api_key, "error.log")
        # 去除本地图片背景
        if file is not None:
            rmbg.remove_background_from_img_file(file)

        #去除网络图片背景色
        if url is not None:
            rmbg.remove_background_from_img_url(img_url=url)

    def changePhotoBackgrColor(self,file,color):
        im = Image.open(file)
        x,y = im.size
        try:
            # RGBA:四通道，RGB为颜色通道，A通道与透明度相关
            p = Image.new('RGBA', im.size, color)
            p.paste(im, (0, 0, x, y), im)
            p.save('2.png')
        except:
            pass

if __name__=='__main__':
    file = r'D:\Learn-python-notes\projects\demo\HandlePhotos\photos\login.jpg'
    # 官网：https://www.remove.bg/
    api_key = "JNr74Jmwtw9SnbipP1LMUG27"
    #颜色对照：https://tool.oschina.net/commons?type=3
    red = (255, 0, 0)
    linen = (250,240,230)
    whilte = (255,255,255)
    blue = (0,0,255)
    handel = HandePhotosDemo()
    handel.getTransparentBackgroPicture(api_key,file)
    # file_1 = r'D:\Learn-python-notes\projects\demo\HandlePhotos\photos\timg.jpg_no_bg.png'
    # handel.changePhotoBackgrColor(file_1,whilte)