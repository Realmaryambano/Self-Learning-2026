# using return
# def avg():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))

#     average = (a+b+c)/3
#     return(f"The average of 3 numbers: {a}, {b}, and {c} is {average}")

# a = avg()
# print(a)


#Function using arguments
def welcome(name = "Maya"):
    return "Welcome " + name

funCall = welcome()
print(funCall)


funCall = welcome("Harry")
print(funCall)

girlName = "Maryam"
funCall = welcome(girlName)
print(funCall)

