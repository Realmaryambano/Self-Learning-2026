# 4. Write a recursive function to calculate the sum of first n natural numbers.

num = int(input("Enter a num: "))
def sum(n):
    if n == 0:            # Base case: sum of 0 numbers is 0
        return 0
    else:
        return n + sum(n-1)

print(f"The sum of {num} natural numbers are ", sum(num))


# sum(5) = 5 + sum(4)
# sum(4) = 4 + sum(3)
# sum(3) = 3 + sum(2)
# sum(2) = 2 + sum(1)
# sum(1) = 1 + sum(0)
# sum(0) = 0  # base case
# Then Python adds them back up: 1+2+3+4+5 = 15 ✅ 
