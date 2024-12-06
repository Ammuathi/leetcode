a=float(input("enter the number"))
b=float(input("enter the number"))

def add(a,b):
    sum=a+b
    return sum
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
ch=int(input("enter the value of choices?"))
if(ch==1):
    data=add(a,b)
    print(data)

elif(ch==2):
    data=sub(a,b)
    print(data)
elif(ch==3):
    data=mul(a,b)
    print(data)
elif(ch==4):
    data=div(a,b)
    print(data)
else:
    print("invalid")
