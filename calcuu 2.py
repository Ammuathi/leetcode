def add(a,b):
    sum=a+b
    print("sum is",sum)
def sub(a,b):
    diff=a-b
    print("difference is",diff)
def mul(a,b):
    prod=a*b
    print("product is",prod)
def div(a,b):
    try:
        quatient = a/b
        print("quatient is",quatient)
    except:
        print("zerodivision")


a=float(input("enter the number"))
b=float(input("enter the number"))
ch=int(input("enter the value of choices?"))
if(ch==1):
    add(a,b)
elif(ch==2):
    sub(a,b)
elif(ch==3):
    mul(a,b)
elif(ch==4):
    div(a,b)
else:
    print("invalid")
