A = {10, 20, 30, 40, 50}
B = {40, 50, 60, 70, 80}
print("Q1")
C= A.union(B)

print(C)
print("\nQ2")
D=A.intersection(B)
print(D)

print("Difference in of A from B:",A-B)

print("Difference in B from A",B-A)

print("Symmetric diff:",A^B)