# 1. Write a program to print multiplication table of a given number using for loop.
print("***** Welcome to Multiplication Table Learner *****")
num = int(input("Enter the number you want the multiplication table for: "))
j = 0

for i in range(0, 100, num):
    print(f'{num} * {j} = ',  i)
    j+=1
