# Overloading
class Overloading:
    def calculator(self, *args):
        print(sum(args))

#Overriding
class Animal:
    def sound(self):
        print('Animal is making sound')

class Dog(Animal):
    def sound(self):
        print('Dog is making sound')

class Cat(Animal):
    def sound(self):
        print('Cat is making sound')

cal = Overloading()
cal.calculator(5,6)
cal.calculator(5,8,9,12)

d = Dog()
c = Cat()
d.sound()
c.sound()