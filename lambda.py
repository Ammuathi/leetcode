from  functools import reduce
nums=[1,2,4,6,8,9]
evens=list(filter(lambda n :n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
print(evens)
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)