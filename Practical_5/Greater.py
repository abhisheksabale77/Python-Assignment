def greater(a,b,c):
    if (a>=b) and (a>=c):
        print("a is greater")
    elif (b>=a) and (b>=c):
         print("b is greater")
    elif (c>=b) and (c>=a):
        print("c is greater")
    else:
        print("All are equal")

greater(5,10,15)
    