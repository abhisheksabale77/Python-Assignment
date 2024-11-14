f1 = open("temp4.txt",'w+')
f1.write("This file is number four")
f1.seek(0)
print(f1.read())
