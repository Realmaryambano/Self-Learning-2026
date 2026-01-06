# Program to find the second largest number in a list without using built-in sort

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

if second_largest == float('-inf'):
    print("No second largest element found.")
else:
    print("Second largest number is:", second_largest)
