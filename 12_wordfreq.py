sentence="python is easy and python is powerful python"
word=sentence.split()

frequency={}

for i in word:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1

print(frequency)