# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

num = int(input("Enter the number: "))
for i in range(1,num+1):
    if i == 1:
        print("* "*num)
    if i != 1 and i != num:
        print("*" + " " * (2*num - 3) + "*")
    if i == num:
        print("* "*num)

"""
num      stars      spaces
        + space
6         11         9
5         9          7
4         7          5
3         5          3
2         3          1
1         2          0
"""