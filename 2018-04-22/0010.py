'''
第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
'''

import string
import random
from PIL import Image, ImageDraw, ImageFont

# 获得任意四个英文字母
def getLetters():
    letters = string.ascii_letters
    str1 = ""
    for i in range(4):
        a = random.choice(letters)
        str1 += a + '   '
    return str1

# 对图片进行处理
def dealImage(str):
    image = Image.open('image.png')
    draw = ImageDraw.Draw(image)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    width, height = image.size
    draw.text((width/2-90, height/2-20), str, font=myfont, fill="#ff0000")
    image.save('result.jpg', 'png')

en = getLetters()
dealImage(en)