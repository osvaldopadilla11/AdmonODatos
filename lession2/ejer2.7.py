f = open("poem_2.txt", "w")

f.write("when I think about myself; ")
f.write("I almost laugh myself to death.")
f.close() # close the file and flush the date in the buffer to the disk
f = open("poem_2.txt","r") # open the file for reading
data = f.read() # read entire file
print(data)
f.close()


         
