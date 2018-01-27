# -*- coding: utf-8 -*-
"""
    将n*n张图片拼接在一起，并覆盖上一张降低透明度的图片
    Copyright: 2018/01/27 by 邵明山
"""

import os
from PIL import Image


def makedir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("The directory \"" + path + "\" creates success.")
    else:
        print("The directory \"" + path + "\" has already existed.")


base_path = "base"
mask_path = "mask"
makedir(base_path)
makedir(mask_path)


n = int(input("Please enter n, n^2 is the number of the pictures."))
print("Please put n^2 pictures to the forder \"base\".")
print("Please put one picture to the forder \"mask\".")
os.system("pause")
width = int(input("Please enter the width of the final picture."))
height = int(input("Please enter the height of the final picture."))
transparency = int(input("Please enter the transparency% of the mask."))

base_pictures = []
for root, dirs, files in os.walk(os.getcwd()+"\\"+base_path):
    for file in files:
        base_pictures.append(os.path.join(root, file))

num = 0
base = Image.new("RGBA", (width, height))
for i in range(0, n):

    for j in range(0, n):
        picture = Image.open(base_pictures[num])
        temp = picture.resize((int(width/n), int(height/n)))
        location = (int(i * width / n), int(j * height / n))
        base.paste(temp, location)
        num += 1

    if num >= len(base_pictures):
        break

    if num >= n*n:
        break

for root, files in os.walk(os.getcwd()+"\\"+mask_path):
    for file in files:
        mask_picture = Image.open(mask_path + "\\" + file)

mask = mask_picture.resize((width, height))
mask.putalpha(int(transparency/100 * 255))

result = Image.alpha_composite(base, mask)
result.save("result.png")
