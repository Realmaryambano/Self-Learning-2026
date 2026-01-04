# Program 1
# Question:
# Write a function 'word_stats(sentence)' that:
# 1. Takes a string sentence as input
# 2. Returns a dictionary with each word as key and its length as value
# 3. Also return a set of unique words
# 4. And a tuple of words longer than 3 letters
# Use loops and string/list methods
# ==========================================
def word_stats(sentence):
    words = sentence.split()
    word_lengths = {}
    long_words = []
    unique_words = set()

    for word in words:
        word_lengths[word] = len(word)
        unique_words.add(word)
        if len(word) > 3:
            long_words.append(word)

    return word_lengths, unique_words, tuple(long_words)

print(word_stats("Python is fun and amazing"))