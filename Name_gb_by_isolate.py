import os

import re

try:
    os.mkdir("output",)
except:
    ...
ls = os.listdir()
ls = [i for i in ls if ".gb" in i]


def get_sample(file_path):
    with open(file_path) as f:
        text = f.read()
    filename = re.findall('/isolate="(.*?)"',text)[0]
    with open("./output/{}.gb".format(filename),"w") as f:
        f.write(text)

for i in ls:
    get_sample(i)