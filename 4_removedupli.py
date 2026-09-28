numbers = [10, 20, 10, 30, 20, 40, 50, 30]
num=[]
for i in numbers:
    if i not in num:
        num.append(i)

print(num)