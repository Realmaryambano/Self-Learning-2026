
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = (a+b+c)/3
print(f"The average of 3 numbers: {a}, {b}, and {c} is {average}")




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

