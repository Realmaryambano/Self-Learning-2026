# ==========================================
# Program 5
# Question:
# Write a function 'unique_characters(strings)' that:
# 1. Takes a list of strings
# 2. Returns a set of all unique characters across all strings
# 3. Returns a dictionary {string: length of string}
# 4. Returns a tuple of strings longer than 4 characters
# ==========================================
def unique_characters(strings):
    unique_chars = set()
    string_lengths = {}
    long_strings = []

    for s in strings:
        string_lengths[s] = len(s)
        unique_chars.update(s)
        if len(s) > 4:
            long_strings.append(s)

    return unique_chars, string_lengths, tuple(long_strings)

# Example run
print(unique_characters(["apple", "banana", "cat", "dog", "elephant"]))