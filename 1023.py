import os

fp = "temp.txt"
#fp = "temp1.txt"

#file = open (fp, "w")


if os.path.exists(fp) :
	print("ok")
	file = open("temp.txt", "a")
else :
	print("error")
	file = open("temp.txt", "w")
	
#file.close()