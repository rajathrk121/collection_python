numbers = (2, 5, 2, 8, 2,2,2,10, 5, 8)

fre={}

for i in numbers:
    if i in fre:
        fre[i]=fre[i]+1
    else:
        fre[i]=1

print(fre)