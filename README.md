# Google EarthView Image Download

Repo, code, and data for downloading images from [Earth View](https://earthview.withgoogle.com/), 
a Google chrome extension that displays a beautiful landscape from Google Earth every time you 
open a new tab.

This repo is an adaptation from Henry Lim's
[earth view repo](https://github.com/limhenry/earthview). 

## Requirements

- python 3.5
- Pillow 5.2.0

The exact python virtual environment can be built using the environment.yml file using conda. The below instructions are for Windows.

## Get Started

1. Use `ev_image_download.py` to download Earth View images. This makes requests to Google's Earth
View database and downloads images listed within a csv file.
2. Use `image_text.py` to add the file name to the downloaded image. This adds the location to the 
upper right corner of each image and saves a copy in another directory. The locations are parsed
from the file names
3. Under Preferences, Background, set your background to Slideshow, and point to the directory where
the downloaded images are stored
