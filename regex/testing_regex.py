import re


def testing_split():
    words = re.split(",", "Hello, this, is, a, sentence, split, by, commas")
    formatted_word = ''.join(word for word in words)
    print(formatted_word)



