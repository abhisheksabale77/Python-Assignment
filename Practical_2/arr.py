import array as arr


a = arr.array('i', [1, 2, 3, 4, 5])


print(a)

a.append(6)
print(a)

a.insert(2, 99)
print(a)

a.remove(99)
print(a)

a.pop(2)
print(a)

a.reverse()
print(a)

index = a.index(4)
print(index)

count = a.count(4)
print(count)

