# 828. Count Unique Characters of All Substrings of a Given String
#
# Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
#
# For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.
#
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
#
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
#
memo = {}


def countUniqueChars(s: str) -> int:
    char_set = set()
    for c in s:
        char_set.add(c)

    i = len(char_set)
    sum = i
    while i > 0:
        sum += (i - 1) ** 2
        i -= 1

    return sum


print(countUniqueChars("ABC"))

print(countUniqueChars("ABA"))
