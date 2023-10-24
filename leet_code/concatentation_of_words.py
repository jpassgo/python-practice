# Given an array of words, which of these words is a concatentation of other words in the array?


def concatentation_of_words(array):
    concatenated_words = []

    is_word_unmodified = True
    for word in array:
        temp_word = word
        temp_array = array.remove(word)
        for other_word in array:
            if is_word_unmodified:
                if temp_word.startswith(other_word):
                    temp_word = temp_word.replace(other_word, "")
                elif temp_word.endswith(other_word):
                    temp_word = temp_word.replace(other_word, "")

                is_word_unmodified = False

            if not is_word_unmodified:
                if temp_word == other_word:
                    concatenated_words.append(word)

    return concatenated_words


print(concatentation_of_words(["cats", "cat", "dogs", "catsdogs", "dog", "catsdog"]))
