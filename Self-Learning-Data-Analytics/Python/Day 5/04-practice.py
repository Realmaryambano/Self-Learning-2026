# ==========================================
# Program 4
# Question:
# Write a function 'frequency_analysis(sentence)' that:
# 1. Takes a string input
# 2. Returns a dictionary with word frequencies (use loops, no .count())
# 3. Returns a tuple of words appearing exactly once
# ==========================================
def frequency_analysis(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    once_words = tuple([word for word, count in freq.items() if count == 1])
    return freq, once_words

# Example run
print(frequency_analysis("Python is fun and Python is powerful"))