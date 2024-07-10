# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:32:10 2024

@author: abhia
"""

import numpy as np

from PIL import Image,ImageDraw
inputImage=Image.open("lena.png")
inputImage.show()

width,height = inputImage.size
print("image width=",width)
print("image height=",height)

pixel_val=list(inputImage.getdata())

pixels=np.array(inputImage.getdata()).reshape(width,height,3)
pixels

print(pixels[0,2,0])
print(pixel_val[1])

for i in range(height):
    inputImage.putpixel((i,i),(0,0,0))
    
inputImage.show()

im_gray=inputImage.convert('CMYK')
im_gray.show()

coordinate=x,y=1,1
print(inputImage.getpixel(coordinate))
print(im_gray.getpixel(coordinate))

txt="not really a fancy text"
imgDrawer=ImageDraw.Draw(inputImage)
imgDrawer.text((5,30),txt)
inputImage.show()
