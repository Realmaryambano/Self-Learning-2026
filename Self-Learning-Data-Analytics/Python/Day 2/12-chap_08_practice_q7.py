# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

num = int(input("Enter number of words you want to enter: "))
wordList = []

def strip_list():
    # Take input from user
    for i in range(num):
        words = input(f"Enter word {i+1}: ")
        wordList.append(words)

    # Show original list (with spaces)
    print("The words that you have entered are:", wordList)

    # Ask which word to remove
    rem = input("Enter the name you want to remove: ").strip()

    # Create final list (stripped + removed)
    finalList = []

    for w in wordList:
        stripped_word = w.strip()
        if stripped_word != rem:
            finalList.append(stripped_word)

    # Show final list
    print("Final list:", finalList)

strip_list()





'''

EXPLANATION OF QUESTION
Input:
words = ["  apple ", "banana", " mango ", "orange "]
word_to_remove = "banana"

What you do:

Strip each word → remove spaces at start and end:
["apple", "banana", "mango", "orange"]

Remove the given word ("banana"):
["apple", "mango", "orange"]

So basically:

Strip spaces → " apple " → "apple"
Remove a word → "banana" is gone
'''