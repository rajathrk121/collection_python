employees = {
"Arun": "IT",
"Rahul": "HR",
"Meera": "IT",
"Anu": "Finance"
}

search ="IT"
fre={}

for name , dep in employees.items():
    if search==dep:
        print(name,':',dep)

for name , dep in employees.items():
    if dep not in fre:
        fre[dep]=1
    else:
        fre[dep]+=1

print(fre)

search_emp=input("Enter employee  name: ")

if search_emp in employees:
    print(employees[search_emp])
else:
    print("No employee found!!!")

name_add=input("Enter employee name: ")

depart=input("Enter dep name: ")

employees[name_add]=depart

print(employees)

name_change=input("Enter employee name: ")
change_dep=input("Enter new dep details: ")

employees[name_change]=change_dep

print(employees)