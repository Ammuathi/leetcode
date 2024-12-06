from functools import reduce
cube=[1,2,3,4]
print(list(map(lambda n:n+3,cube)))
def pos(num):
    return True if num>0 else False
print(list(filter(pos,[1,2,-3,7,-9,4])))
print(list(filter(lambda num: num.isupper(),'aPpLE')))
def sum_list(x,y):
    return x+y
print(reduce(sum_list,[1,2,3,4,5]))