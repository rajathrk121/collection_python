tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
tuple3=()
for i in tuple1:
    if i in tuple2:
        tuple3=tuple3 + (i,)
print(tuple3)