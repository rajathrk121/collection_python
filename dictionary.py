# student = {
#     "name": "Rajath",
#     "age": 21,
#     "course": "Python",
#     "mark": 85
# }

# for name,i in student.items():
#     print(name , i)

# backup=student.copy()
# print(backup)

# student.update({
#     "city":"kozhikode",
#     'grade':"A",
#     'mark': 90
# })
# remove=student.popitem()
# student.clear()
# print(student)

# sentence = "python is easy and python is powerful"
# sp_sentence=sentence.split()
# frequency={}

# for i in sp_sentence:

#     if i in frequency:
#         frequency[i]=frequency[i]+1
#     else:
#         frequency[i]=1

# print(frequency)

students = {
    "Arun": [80, 75, 90],
    "Rahul": [70, 85, 78],
    "Anu": [95, 92, 88]
}
high=0
low=100
avg_student={}

for name,mark in students.items():
    total=sum(mark)
    average=total/len(mark)

    print(name,':',average)

    if average>high:
        high=average
        high_name=name

    if average<low:
        low=average
        low_name=name

    if average>50:
        avg_student[name]=mark


print(high_name,':',high)
print(low_name,':',low)
print(avg_student)
