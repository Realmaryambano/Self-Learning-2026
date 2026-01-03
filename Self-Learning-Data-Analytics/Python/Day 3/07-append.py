string = "This is a new file"
f = open("09-new_file.txt","w")
f.write(string)
f.close()

h = open("08-append.txt","a")
h.write(string)
h.close

