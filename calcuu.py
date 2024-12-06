    def add():
    print("sum is",a+b)
def sub():
    print("differenec is ",a-b)
def mul():
    print("product is",a*b)
def div():
    try:
        print("quatient is",a/b)
    except:
        print("zerodivision")


a=float(input("enter the number"))
b=float(input("enter the number"))
ch=int(input("enter the value of choices?"))
if(ch==1):
    add()
elif(ch==2):
    sub()
elif(ch==3):
    mul()
elif(ch==4):
    div()
else:
    print("invalid")
