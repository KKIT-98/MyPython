# _*_ coding:utf-8 _*_
import os

import cv2
from PIL import Image

"""
PNG图像无损放大
"""


imgPath = './2024031714041.png'
newImgPath = './new202403171404.png'
# 读取原图片的像素RGB值 读取图片
img = Image.open(imgPath)

# 无损放大

new_size = (1580, 1060)
result_img = img.resize(new_size, resample=Image.BICUBIC)

# 写入保存图像
result_img.save(newImgPath)


