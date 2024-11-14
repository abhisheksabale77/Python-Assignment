def fun1(n):
    if(n==0 or n==1 ):
        return 0
    else:
        for i in range(2,n):
            if(n%i == 0):
                return 0
                break
x = int(input("Enter a number : "))
if(fun1(x)==0):
    print("Not prime")
else:
    print("Is prime")
    

    