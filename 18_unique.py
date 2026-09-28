seq=input("Enter the sequence: ")

sequen=seq.split()

seq_set=set(sequen)
print(seq_set)
print("Number of unique words:", len(seq_set))