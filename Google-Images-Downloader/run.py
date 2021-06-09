import google_images_download
import os

#Put The Names of Plant inside Data String Below
# i.e data = 'Plant_1, Plant_2, Plant_3, ...... , Plant_n']

data = 'Acca sellowiana, Acer negundo, Muscari armeniacum'


# Run The Script So It will Start Downloading Images From The Google
# Set The Limit That How Many Images you Want to Download From Google
try:
    os.system('googleimagesdownload --keywords "'+data+'" --size medium --limit 100')
except Exception as e:
    print("Exception Occured :- ", e)


# The Images Will Be Downloaded to Downloads Folder
