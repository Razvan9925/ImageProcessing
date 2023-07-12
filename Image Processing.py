from skimage import io
from skimage import color
import re
import numpy as np 
from PIL import Image
from pathlib import Path

import sys

img = io.imread(r"E:\tsts\parrots.bmp")
img_xyz = color.rgb2xyz(img)
img_rgb = color.xyz2rgb(img_xyz)

with open('rgb.txt','a') as sys.stdout:
    print(img_rgb)
    
with open('xyz.txt','w') as sys.stdout:
    print(img_xyz)

img2=io.imsave('E:/tsts/parrots2.bmp',img_rgb)
img3=io.imsave('E:/tsts/parrots3.bmp',img_xyz)

img1 = io.imread(r"E:\tsts\myXYZ.txt")
img1_rgb = color.xyz2rgb(img1)
