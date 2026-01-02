# 6. Write a python function which converts inches to cms.

inches = float(input("Enter inches to convert into cm: "))

def inch_to_cm(inches):
    return inches * 2.54

print(inch_to_cm(inches))

# Using :.2f formats the number to 2 decimal places.
# Note: .2f is NOT a method or attribute of a number.
# It is a format specifier used inside f-strings, format(), or % formatting.
print(f"{inches} inches is {inch_to_cm(inches):.2f} cm")
