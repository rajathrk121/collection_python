student={
    'Rajath':40,
    'Abhi':45,
    'Adhin':35,
    'Karthik':20,
    'Adil':30
}
print('\nQ1')
for i in student.keys():
    print(i)
print('\nQ2')
for mark in student.values():
    print(mark)
print('\nQ3')
highest=0
highes_stu=""
for name in student:
    if student[name]>highest:
        highest=student[name]
        highes_stu=name
print (highes_stu,highest)
print('\nQ4')
l=len(student)
sum=0
for mark in student.values():
    sum+=mark
average=sum/l
print("average:",average)

