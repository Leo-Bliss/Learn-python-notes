#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/7 0007 20:58
#@Author  :    tb_youth
#@FileName:    QRCode.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import qrcode
from  pyzbar import  pyzbar
from PIL import  Image
import cv2

#从中心开始裁减图片
def cut_image(image, x, y):
    x_center,y_center = image.width / 2,image.height / 2
    new_x1,new_y1 = x_center - x//2,y_center - y//2
    new_x2,new_y2 = x_center + x//2,y_center + y//2
    new_image = image.crop((new_x1, new_y1, new_x2, new_y2))
    return new_image


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取二维码的边界框的位置
        (x, y, w, h) = barcode.rect
        # 画出图像中条形码的边界框
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #提取二维码中的数据
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 输出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)

        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image




class QRCodeDemo(object):
    def __init__(self):
        self.qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4,
        )
    #生成二维码
    def create(self,data,fill_color,back_color):
        #设置二维码数据
        self.qr.add_data(data=data)
        #设置二维码颜色
        self.qr.make(fit=True)
        image = self.qr.make_image(fill_color=fill_color,back_color=back_color)
        return image

    #扫描二维码
    def scan(self,image):
        scaner = pyzbar
        codes = scaner.decode(image)
        data = ''.join([code.data.decode('utf-8') for code in codes])
        print('二维码的内容为:\n',data)
        print('-'*100)
        return data

    #设置二维码背景
    def compose(self,image,bkg,alp=0.4):
        image = Image.open(image)
        background = Image.open(bkg)
        new_background = cut_image(background,image.width,image.height)
        final_image= Image.blend(image,new_background,alpha=alp)
        return final_image

    #打开摄像头扫描二维码
    def online_scan(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret,frame = camera.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            img = decodeDisplay(gray)
            cv2.waitKey(5)
            cv2.imshow("camera", img)

        camera.release()
        cv2.destroyAllWindows()


if __name__=='__main__':
    qr = QRCodeDemo()

    # image = qr.create('flag{I_Love_U}','blue','white')
    # image.show()
    # image.save('./images/1.jpg')


    image = Image.open('./images/1.jpg')
    qr.scan(image)

    # cp_image = qr.compose('./images/1.jpg','0.jpg')
    # cp_image.show()
    # cp_image.save('./images/0_1.jpg')
    # image = Image.open('./images/0_1.jpg')
    # qr.scan(image)
    # qr.online_scan()







