f1 = open('temp.txt', 'a+')
f1.write("APENDING")
f1.seek(0)
print(f1.read())

