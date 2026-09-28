class_a = {"Arun", "Rahul", "Akhil", "Meera", "Anu"}
class_b = {"Meera", "Anu", "Vishnu", "Rahul", "Riya"}

inboth=class_a.intersection(class_b)
print(inboth)
print(class_a.difference(class_b))
print(class_b.difference(class_a))

unique=class_a.union(class_b)

print(unique)
