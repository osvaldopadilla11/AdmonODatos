f = open("poem_2.txt", "w")
print("when I think about myself," , file=f)
print("I almost laugh myself to death.", file=f)
f.close()
f = open("poem_2.txt", "r") # openthe file again
data = f.read()
print(data)