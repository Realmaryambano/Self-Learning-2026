# . py is also a textual file

# Reading a file
f = open("02-file.txt")
data = f.read()
print(data)
f.close()

# practice
f_to_read = open("02-file.txt")
data = f_to_read.read()
print(data)
f_to_read.close()