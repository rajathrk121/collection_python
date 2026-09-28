list=[2,7,8,9,5,2,4,63,15,7,1,4,7,4]

largest=list[0]
sec_largest=list[0]

for num in list:
    if num>largest:
        sec_largest=largest
        largest=num
    elif num>sec_largest and num!=largest:
        sec_largest=num

print(sec_largest)