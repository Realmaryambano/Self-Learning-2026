# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

print("***** Welcome to Multiplication Table Learner *****")
num = int(input("Enter the number you want the multiplication table for: "))

for i in range(10, 0,-1):
    print(f'{num} * {i} = {i*num}')
    i=i-1