a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the value of operation"))
if(c==1):
    print("addition")
    c=a+b
    print(c)
elif(c==2):
    print("subtraction")
    c=a-b
    print(c)
elif(c==3):
    print("multiplication")
    c=a*b
    print(c)
elif(c==4):
    if(b!=0): 
        print("division")
        c=a/b
        print(c)
    else:
        print("undefined")
else:
    exit()
