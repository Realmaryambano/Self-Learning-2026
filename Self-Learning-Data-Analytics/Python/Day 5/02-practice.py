# ==========================================
# Program 2
# Question:
# Write a function 'count_vowels(sentence)' that:
# 1. Takes a string input
# 2. Counts vowels in the string and stores in a dictionary {vowel: count}
# 3. Returns the dictionary and a list of vowels that appear at least once
# ==========================================
def count_vowels(sentence):
    vowels = 'aeiou'
    sentence_lower = sentence.lower()
    vowel_count = {}
    vowels_found = []

    for ch in sentence_lower:
        if ch in vowels:
            if ch in vowel_count:
                vowel_count[ch] += 1
            else:
                vowel_count[ch] = 1

    vowels_found = list(vowel_count.keys())
    return vowel_count, vowels_found

# Example run
print(count_vowels("Hello World, Python is amazing"))