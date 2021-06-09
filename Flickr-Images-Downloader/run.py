import scraper
import time
import os
import sys

#Put The Names of Plant inside Data List Below
# i.e data = ['Plant_1', 'Plant_2', 'Plant_3', ...... , 'Plant_n']
data = []

# data = ['Acca sellowiana','Acer negundo', 'Muscari armeniacum']

def flickr():
    for i in data:
        try:
            os.system('python scraper.py --search "'+i+'" --max-pages 1 --start-page 0')
        except Exception as e:
            print("Exception Occured :- ", e)

# Run The Script So It will Start Downloading Images From The Flickr
flickr()
