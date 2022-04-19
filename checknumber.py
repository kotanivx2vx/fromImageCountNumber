from PIL import Image
import pyocr
import cv2
import re
import pandas as pd
import os

# prepare tesseract

def kankoredata(path):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    
    img_kankore =Image.open(path)
    kankore_txt = tool.image_to_string(
    img_kankore,
    lang= "eng",
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    pat = r"\d+"
    number = []
    num =  re.findall(pat, kankore_txt)
    return num

# make numbers from photo
def make_nums():
    dir_name = "/content/drive/MyDrive/last_kankore"
    nums=[]
    files = os.listdir(dir_name)
    for file in files:
        if not file.startswith("."):
            path = os.path.join(dir_name,file)
            num =  kankoredata(path)
            nums.append(num)
    return nums

# make data from numbers
def countcheck(nums) :
    df=pd.DataFrame(nums)
    df.columns = ["火力","雷装","対空","対潜","索敵","運"]
    df = df.astype({"火力":int,"雷装":int,"対空":int,"対潜":int,"索敵":int,"運":int})
    sum = df.sum()
    df.to_csv("countcheck.csv",index = False, encoding="utf-8")
    return sum

if __name__ == "__main__":
    nums = make_nums()
    sum = countcheck(nums)
    print(sum)
