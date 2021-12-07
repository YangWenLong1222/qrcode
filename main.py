#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image
import numpy as np
from time import sleep
import os

def main():
    # 1, 获取二维码文件列表。
    fileList = os.listdir('qrcode')
    print(fileList)
    # 2, 打开海报图片。
    for qr_name in fileList:
        img = Image.open('haibao.jpeg')
        qr = Image.open('qrcode/' + qr_name)
        img.paste(qr, (430, 90)) #TODO: 坐标要调整。
        img.save('result/hb_'+qr_name, quality=95)
    # print(img.format)
    # print(img.size)  # 注意，省略了通道 (w，h)
    # print(img.mode)  # L为灰度图，RGB为真彩色,RGBA为加了透明通道
    # img.show()  # 显示图片
    # qr.show()
    return

if __name__ == '__main__':
    main()
