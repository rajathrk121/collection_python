import calculator

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

print("1. Add \n2. Subtract \n3. Multiply \n4. Divide")
choice = int(input("Enter your choice"))

match choice:
    case 1:
        calculator.add(num1,num2)
    case 2:
        calculator.subtract(num1,num2)
    case 3:
        calculator.multiply(num1,num2)
    case 4:
        calculator.divide(num1,num2)
    case _:
        print("Error!!!!!\nEnter a valid choice")