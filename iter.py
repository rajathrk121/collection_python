numbers = [11, 24, 35, 42, 57, 68, 73, 80]

x = iter(numbers)

while True:
    num = next(x)
    
    if num%2:
        print(num)