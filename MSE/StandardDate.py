f1 = open("date.txt",'r')
date = f1.readlines()
print(date)
l = date.__len__()
print(l)
print(date[0])
d = []
d.insert(1,date[0].strip('\n'))
print[d]
# D = []
# for i in range(0,l):
#     d[0] = date[0].strip('\n')
#     D[0]= d[0].split('/' or '.' or '-')


# d1 = []
# for j in range(0,l):
#     for i in range(1,3) :
#         T = D[j]
#         d1[j]+=T[-i]
#         d1[j]+='-'

#     d1[j]+=T[-3]

# for i in d1:
#     print(d1)

# print(d2)

    
