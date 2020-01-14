#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Python:         3.5.3
Purpose:     	Add text to images in a folder
Description: 	This script will add file names to images.
                It will keep the original images and save
                renamed copies of the image into the selected folder.
Author:      	Stephen Morgan, GISP
Date Created:   02/20/2019
'''

# import modules
from PIL import ImageDraw, Image, ImageFont
import os

# change these per your requirements
image_folder = r"E:\Python\Projects\EarthView_Wallpaper\Image_Download\\"
output_folder = r"E:\Python\Projects\EarthView_Wallpaper\Image_Download\Text_Added"
font_file = r"E:\Python\Projects\EarthView_Wallpaper\Font\arial.ttf"
extensions = ["JPG"]

for image in os.listdir(image_folder):
    if os.path.isfile(os.path.join(image_folder, image)):
        f_text, f_ext = os.path.splitext(image)
        f_ext = f_ext[1:].upper()
        output = os.path.join(output_folder, image)
        if f_ext in extensions:
            print(image)
            new_name = output.strip(".jpg")
            img = Image.open(os.path.join(image_folder, image))
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(font_file, 16)
            draw.text((5, 2), image, (255, 255, 255), font=font)
            img.save(new_name + '_addtext.jpg', quality=500)

print("\nValar Morghulis")
