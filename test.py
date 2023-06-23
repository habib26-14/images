import os
import shutil
from PIL import Image

if os.path.exists("temp") is False:
    os.mkdir("temp")

for i in os.listdir("images"):
    if i != ".DS_Store":
        tmp = "images/" + i
        img = Image.open(tmp)
        img.rotate(-90)
        img.resize((128, 128))
        img = img.convert("RGB")
        img.save(i+".jpeg")
        shutil.move(i+".jpeg", "temp/")
