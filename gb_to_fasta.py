import os

try:
	os.mkdir("output")
except:
	...

def gb_to_fas(gb_file):
	with open(gb_file) as f:
		ls = f.readlines()

	text = ""
	flag = 0
	for i in ls:
		if flag:
			for j in i:
				if j in "atcg":
					text += j
		if "ORIGIN" in i:
			flag = 1
	with open("./output/{}.fas".format(gb_file.replace(".gb","")),"w") as f:
		f.write(">"+gb_file.replace(".gb","")+"\n")
		f.write(text)

ls = os.listdir()
ls = [i for i in ls if ".gb" in i]

for i in ls:
	gb_to_fas(i)