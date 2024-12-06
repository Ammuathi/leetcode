a=float(input("enter the number"))
b=float(input("enter the number"))

def add():
    sum=a+b
    return sum
def sub():
    diff=a-b
    return(diff)
def mul():
    prod=a*b
    return(prod)
def div():
    try:
        quatient = a/b
        return(quatient)
    except:
        print("zerodivision")
ch=int(input("enter the value of choices?"))
if(ch==1):
    data=add()
    print(data)

elif(ch==2):
    data=sub()
    print(data)
elif(ch==3):
    data=mul()
    print(data)
elif(ch==4):
    data=div()
    print(data)
else:
    print("invalid")
