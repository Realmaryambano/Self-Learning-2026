# 3. Attempt problem 1 using while loop.
print("***** Welcome to Multiplication Table Learner *****")
num = int(input("Enter the number you want the multiplication table for: "))
j = 0
while(j<=10):
        print(f'{num} * {j} = ',  j*num)
        j+=1

