# 6. Write a program to calculate the factorial of a given number using for loop.
num = int(input("Enter the number for factorial: "))
i = 1
factorial = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial:", factorial)
