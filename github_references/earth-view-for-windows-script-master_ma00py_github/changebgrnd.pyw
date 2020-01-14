import urllib.request
from random import randint
import linecache
import ctypes; import os

def change():
    dataref = open("bgnlist1.txt")
    num_lines = sum(1 for line in dataref)
    url=linecache.getline("bgnlist1.txt", randint(0, num_lines))
    urllib.request.urlretrieve(url, "background.jpg")
    path=os.getcwd() + "\\" + '''background.jpg'''
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
change()
