
t = (1, 2, 3, 2, 4, 2, 5)

count = t.count(2)
print(count)  

index= t.index(2)
print(index )  


t2 = t + (6, 7)
print(t2)  
 
print(t[1:4])  

a, b, c, d, e, f, g = t
print(a,b,c,d,e,f,g)  

t.__add__(t2)
print(t)

