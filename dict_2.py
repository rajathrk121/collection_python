students = {
    "Arun": 85,
    "Rahul": 72,
    "Anu": 95,
    "Ravi": 60
}
high=0
# high_name=''
low=100
# student=input('Enter the name of the student:')
for name , mark in students.items():
    # if name==student:
    #     print(name,':',mark)
    # else:
    #     print("Student not found")
    # print(name,':',mark)
    if mark>high:
        high=mark
        high_name=name
    if mark<low:
        low=mark
        low_name=name

print("Highest mark student:",high_name,':',high)
print("Lowest mark student:",low_name,':',low)
s=0
for mark in students.values():
    s+=mark
    average=s/len(students)
print("Total average is :",average)