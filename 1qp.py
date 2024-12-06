def bmi_index(weight,height):
    return weight/(height**2)
weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in m:"))
bmi  = bmi_index(weight,height)
print("your BMI is",bmi)
