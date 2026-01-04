def analyze_sentence(sentence):
    # convert to lowercase and split into words (string → list)
    words_list = sentence.lower().split()

    # dictionary to store word counts
    word_count = {}

    # loop to count words
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # set of unique words
    unique_words = set(words_list)

    # list to store repeated words
    repeated_words = []

    # loop through dictionary to find words appearing more than once
    for word, count in word_count.items():
        if count > 1:
            repeated_words.append(word)

    # convert list to sorted tuple
    repeated_words_tuple = tuple(sorted(repeated_words))

    # return required values
    return words_list, word_count, repeated_words_tuple

sentence = "Python is fun and Python is powerful"
result = analyze_sentence(sentence)
print(result)
