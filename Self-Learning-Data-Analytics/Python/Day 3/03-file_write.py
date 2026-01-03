string_to_write = "Hello new file... I am going to write in you hehe"

f = open("04-my_file.txt","w") # w is must for writing or making a new file4
f.write(string_to_write) # write; not writable
f.close()