import os
from PIL import Image
import cv2


last_dir_name = "last_kankore"   #send photos to next 
new_dir_name = "num_kankore"     #check photos
dir_name = "kankore"             #prepare photos   

THRESH_MIN, THRESH_MAX = (160, 255)
THRESH_MODE = cv2.THRESH_BINARY_INV

files = os.listdir(dir_name)
for file in files:
    if not file.startswith("."):
        #cut image
        img = Image.open(os.path.join(dir_name,file))
        cut_img = img.crop((1110,630,1165,850))       #select cuting zone
        cut_img.save(os.path.join(new_dir_name, file))
        #image create
        img_src = cv2.imread(os.path.join(new_dir_name, file))
        gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
        img_bin = cv2.threshold(gray, THRESH_MIN, THRESH_MAX, THRESH_MODE)[1]
        image2 = cv2.bitwise_not(img_bin)
        cv2.imwrite(os.path.join(last_dir_name, file), image2)