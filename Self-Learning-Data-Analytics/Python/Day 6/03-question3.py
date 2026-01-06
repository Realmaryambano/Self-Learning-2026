# Program to count frequency of each character in a string using a dictionary

text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for key, value in frequency.items():
    print(key, ":", value)
