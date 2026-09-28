list=[2,8,7,5,1,3,9,4,]

even=[]
odd=[]

for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
