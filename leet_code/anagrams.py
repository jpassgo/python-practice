def groupAnagrams(words):
    anagrams_by_len = {}

    for word in words:
        if len(word) in anagrams_by_len.keys():
            anagrams_of_word_len = anagrams_by_len[len(word)]
            for anagrams in anagrams_of_word_len:
                if anagram_matches(anagrams[0], word):
                    anagrams.append(word)
                    break
            anagrams_of_word_len.append([word])
        else:
            anagrams_by_len[len(word)] = [[word]]

    anagrams = []
    for anagrams_of_len in anagrams_by_len:
        [anagrams.append(anagram) for anagram in anagrams_by_len[anagrams_of_len]]

    return anagrams

def anagram_matches(anagram, word): 
    for letter in word:
        if letter in anagram:
            anagram.replace(letter, '', 1)
        else:
            return False

    return True


print(groupAnagrams(['foo', 'flop', 'olfp','yo','act','oy','cat','tac']))