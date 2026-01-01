# 4. Write a program to find whether a given number is prime or not.
print("** PRIME NUMBER CALCULATOR **")
num = int(input("Enter the number: "))

if num < 2:
    print("Number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
