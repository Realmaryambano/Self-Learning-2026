# using return
# def avg():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))

#     average = (a+b+c)/3
#     return(f"The average of 3 numbers: {a}, {b}, and {c} is {average}")

# a = avg()
# print(a)

# Function using arguments with a default parameter
def welcome(name="Maya"):  # 'name' has a default value of "Maya"
    return "Welcome " + name  # Returns a greeting string

# Function call without argument
funCall = welcome()  # Uses default parameter 'name="Maya"'
print(funCall)       # Output: Welcome Maya

# Function call with an argument
funCall = welcome("Harry")  # Overrides default, 'name' becomes "Harry"
print(funCall)               # Output: Welcome Harry

# Function call with a variable as argument
girlName = "Maryam"
funCall = welcome(girlName)  # Passes variable 'girlName' to 'name'
print(funCall)               # Output: Welcome Maryam
