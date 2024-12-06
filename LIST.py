'''fruits=["apple","banana","grapes","orange"]
newlist=[]
for fruit in fruits:
    if 'n' in fruit:
        newlist.append(fruit)
print(newlist)



result= [fruit for fruit in fruits if 'n' in fruit]
print(result)'''                                  

l=[1,2,3,5]
result=(list(map(lambda n:n*2,l)))
print(result)
output=(n*2 for n in l)
print (list(output))