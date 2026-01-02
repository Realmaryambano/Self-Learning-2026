# 8. Write a python function to print multiplication table of a given number.

num = int(input("Enter a number for multiplicaton: "))

def mul(num):
    for i in range(1,11):
        print(f"{num} * {i} = ", num*i)

mul(num)

