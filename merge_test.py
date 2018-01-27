import os
from PIL import Image

# import pyautogui
# import re
'''
把当前目录下的10*10张jpeg格式图片拼接成一张大图片

'''

# 图片压缩后的大小
# width_i = 200
# height_i = 300
width_i = 455
height_i = 455

# 每行每列显示图片数量
line_max = 5
row_max = 5

# 参数初始化
all_path = []
num = 0
pic_max = line_max * row_max

dirName = os.getcwd()

for root, dirs, files in os.walk(dirName):
    for file in files:
        if "jpg" in file:
            all_path.append(os.path.join(root, file))

toImage = Image.new('RGBA', (width_i * line_max, height_i * row_max))

for i in range(0, row_max):

    for j in range(0, line_max):
        pic_fole_head = Image.open(all_path[num])
        width, height = pic_fole_head.size

        tmppic = pic_fole_head.resize((width_i, height_i))
        # tmppic = pic_fole_head.resize((int(width / 3), int(height / 3)))

        loc = (int(i % line_max * width_i), int(j % line_max * height_i))

        # print("第" + str(num) + "存放位置" + str(loc))
        toImage.paste(tmppic, loc)
        num += 1

    if num >= len(all_path):
        print("break")
        break

    if num >= pic_max:
        break

print(toImage.size)
toImage.save('merged.png')