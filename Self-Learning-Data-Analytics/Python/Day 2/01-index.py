""" 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = (a+b+c)/3
print(f"The average of 3 numbers: {a}, {b}, and {c} is {average}")
"""


'''
# now making function
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    average = (a+b+c)/3
    print(f"The average of 3 numbers: {a}, {b}, and {c} is {average}")

for i in range(5):
    print(f"Average Calculator for user {i+1}")
    avg()
'''
# () → no parameters passed
# enumerate() is a built-in function
# it returns index and value as a pair
# start=1 means counting starts from 1 instead of 0
# () → parentheses used to pass parameters (empty here, so no arguments)


names = ["maryam", "ayesha", "shruti"]

for index, name in enumerate(names, start=1):
    print(index, name)

# Function using enumerate
def avg_res():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    average = (a+b+c)/3
    print(f"The average of 3 numbers: {a}, {b}, and {c} is {average}")

name = ["maryam","ayesha","shruti"]

for index,i in enumerate(name, start=1):
    print(f"Average Calculator for user {index}.{i.title()}: ")
    avg_res() # this is a function call 
