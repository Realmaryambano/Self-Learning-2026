for i in range(100):
    if i == 50:
        print(i) # Only prints i when i is 50

for i in range(15):
    if i == 4+1:
        break # for loops end here if condition is true
    else:
        print(i)

for i in range(15):
    if i == 11:
        continue # skip this iteration
    else:
        print(i) # prints all except the above iteration