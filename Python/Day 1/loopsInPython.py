#Loops in python

# Quick Quiz: Write a program to print 1 to 50 using a while loop.
i = 1
while(i<=50):
    print(i, "Maryam")
    i+=1

for i in range (0,51):
    print(i, "Maryam")
    i+=1

i = 1
while(i>=6): #Condition false so nothing will run
    print(i)


while(i>=6): #Condition false so nothing will run and increment won't happen as condition is false
    print(i)
    i=i+1


while(i<=6): #Condition true so it will run until the condition is false from 1,2,3,4,5,6
    print(i)
    i=i+1

while(i>=6): #  If here i was actually greater than 6 like i=7, then it would cause infinite loop each time it increment
    print(i)
    i=i+1


for i in range(0,5):
    print(i)

print("\n")

for i in range(1,5):
    print(i)
print("\n")

for i in range(5):
    print(i)
print("\n")

for i in range(1,6):
    print(i)
print("\n")

for i in range(1,5+1):
    print(i)
print("\n")

