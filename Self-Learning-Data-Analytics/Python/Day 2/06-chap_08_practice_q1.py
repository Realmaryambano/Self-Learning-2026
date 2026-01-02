# 1. Write a program using functions to find greatest of three numbers.
def greatestnum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    greatest = num1  # assume num1 is greatest initially

    if num2 > greatest:
        greatest = num2
    if num3 > greatest:
        greatest = num3

    print(f"The greatest number from {num1}, {num2}, and {num3} is {greatest}")

greatestnum()


greatestnum()
# 1. Write a program using list to find greatest of three numbers.

# num = []
# for i in range(5):
#     number = input(f"Enter number {i+1}: ")
#     num.append(number)
# print("The numbers are: ", ", ".join(num))