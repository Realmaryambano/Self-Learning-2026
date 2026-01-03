f = open("06-string.txt")
data = f.readlines() # for reading all lines
print(data,type(data))
f.close()



h = open("06-string.txt")

line1 = h.readline() # for reading one line
print(line1,type(line1))

line2 = h.readline() 
print(line2,type(line2))

line3 = h.readline() 
print(line3,type(line3))

line4 = h.readline() 
print(line4,type(line4))

line5 = h.readline() 
print(line5,type(line5))

line6 = h.readline() 
print(line6,type(line6))

line7 = h.readline() 
print(line7,type(line7))

line8 = h.readline()
print(line8,type(line8))
h.close()


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()