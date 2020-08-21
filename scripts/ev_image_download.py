#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Python:         3.5.3
Purpose:     	Download images from EarthView
Author:         Stephen Morgan, GISP
Date Created:   02/19/2019
'''

import urllib.request
import os
import csv

image_list_csv = r"..\Data\ev_list_scrub_removedquestion.csv"
download_folder = r"..\Image_Download"


def download_image(file_path):
    with open(image_list_csv, 'r') as csvfile:
        rcsv = csv.reader(csvfile, delimiter=',')
        for row in rcsv:
            url = 'http://' + row[1]
            image_name = row[2]
            print("image: ", image_name)

            full_path = os.path.join(download_folder, image_name)
            urllib.request.urlretrieve(url, full_path)


if __name__ == '__main__':
    download_image(download_folder)

print("\nValar Morghulis")
