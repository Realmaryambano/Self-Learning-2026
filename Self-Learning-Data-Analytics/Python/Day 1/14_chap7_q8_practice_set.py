# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

num = int(input("Enter the number: "))
for i in range(1,num+1):
    print("*" * (i))
