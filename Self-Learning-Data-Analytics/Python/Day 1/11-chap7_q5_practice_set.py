# 5. Write a program to find the sum of first n natural numbers using while loop.
num = int(input("Enter the number for sum: "))
i = 0
total = 0
while i <= num:
    total += i
    i += 1
print("Sum:", total)
