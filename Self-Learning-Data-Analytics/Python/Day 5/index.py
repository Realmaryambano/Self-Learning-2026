# =========================================================
# Question:
# Write a Python program that does the following in one function:
# 1. Takes a sentence as input (string)
# 2. Splits the sentence into words and stores them in a list
# 3. Converts all words to lowercase
# 4. Creates a set of unique words
# 5. Creates a dictionary with word counts (using loops, no .count())
# 6. Creates a tuple of words that appear more than once, sorted alphabetically
# 7. Returns a list of words longer than 3 characters
# 8. Counts vowels in the sentence and returns a dictionary {vowel: count}
# 9. Returns a tuple of words that start with a vowel
# 10. All results should be returned from one function
# =========================================================

def analyze_text(sentence):
    # Step 1-3: string → list (lowercase)
    words_list = sentence.lower().split()

    # Step 4: set of unique words
    unique_words = set(words_list)

    # Step 5: word count dictionary
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Step 6: tuple of repeated words (alphabetically)
    repeated_words = tuple(sorted([word for word, count in word_count.items() if count > 1]))

    # Step 7: list of words longer than 3 characters
    long_words = [word for word in words_list if len(word) > 3]

    # Step 8: count vowels in the sentence
    vowels = 'aeiou'
    vowel_count = {}
    for ch in sentence.lower():
        if ch in vowels:
            if ch in vowel_count:
                vowel_count[ch] += 1
            else:
                vowel_count[ch] = 1

    # Step 9: tuple of words starting with a vowel
    vowel_start_words = tuple([word for word in words_list if word[0] in vowels])

    # Step 10: return all results
    return {
        "words_list": words_list,
        "unique_words": unique_words,
        "word_count": word_count,
        "repeated_words": repeated_words,
        "long_words": long_words,
        "vowel_count": vowel_count,
        "vowel_start_words": vowel_start_words
    }

# =========================================================
# Example Run
# =========================================================
sentence = "Python is fun and Python is powerful"
results = analyze_text(sentence)

print("List of words:", results["words_list"])
print("Set of unique words:", results["unique_words"])
print("Word counts:", results["word_count"])
print("Repeated words tuple:", results["repeated_words"])
print("Words longer than 3 chars:", results["long_words"])
print("Vowel counts:", results["vowel_count"])
print("Words starting with a vowel:", results["vowel_start_words"])
