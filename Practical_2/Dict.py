d = {
    'name': 'Digambar',
    'age': 20,
    'city': 'Ajara'
}

print(d)

d1 = d.copy()  
print(d1) 

d1.clear()
print(d1)

age = d.get('age')
print(age)  

items = d.items()
print(items) 

keys = d.keys()
print(keys)  

d.pop("age")
print(d)  

values = d.values()
print(values)  
