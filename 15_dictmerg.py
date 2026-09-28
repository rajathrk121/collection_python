dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"d": 40, "e": 50, "f": 60}

dict3={}

for i in dict1:
    dict3[i]=dict1[i]
for i in dict2:
    dict3[i]=dict2[i]
print(dict3)