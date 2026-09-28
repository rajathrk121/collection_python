# students = {
# "Arun": [80, 75, 90],
# "Rahul": [70, 85, 78],
# "Anu": [95, 92, 88]
# }

# for name,mark in students.items():
#     average=sum(mark)/len(mark)
#     print(name,average)
#     highest=0
#     highestname=''
#     if average>highest:
#         highestname=name
#         print(highestname)


# print(highestname)

student = {
    "name": "Rajath",
    "age": 21,
    "mark": 85
}

print(student.get("name"))
print(student["age"])
student['city']="Kozhikode"
student['mark']=90
student.pop('age')
print(student)