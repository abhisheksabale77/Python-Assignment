s= {1,2,3,4}

s.add(4) 
print(s)

s.remove(2) 
print(s) 

s.discard(1) 
print(s)

s.pop()
print(s)

s.clear()
print(s)

s1 = {1,2,3,4}
s2 = {4,5,6}

result = s1.union(s2)
print(result)

result = s1.intersection(s2)
print(result)

s1.update(s2)
print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.difference(s2)
print(result)  

s1.clear()
s1 = s2.copy()
print(s1)
