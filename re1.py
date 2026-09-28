import re

text = "I have 10 apples, 25 bananas and 3 oranges."

a=re.findall(r"\d+",text)

print(a)

text = "Hello, welcome to Python"
b=re.search(r"^Hello",text)
if b:
    print("Starts with hello")

text = "www.com google "
c=re.search(r"com$",text)
if c:
    print("Ends with com")

text = "Python is easy to learn"
d=re.match(r"Python",text)
if d:
    print('match found')