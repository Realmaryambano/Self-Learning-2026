# Program to check whether a given string is a palindrome ignoring case and spaces

string = input("Enter a string: ")

cleaned = string.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
