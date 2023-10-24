#
# Using sliding window technique to determine largest range of non repeating characters in a string.
#
from collections import defaultdict


def longest_unique_substring(s):
    s_len = len(s) - 1

    longest_substring = float("-inf")

    left, right = 0, 0
    window = defaultdict(int)
    while right < s_len:
        right_character = s[right]
        window[right_character] += 1
        right += 1

        while window[right_character] > 1:
            left_character = s[left]
            window[left_character] -= 1
            left += 1

        longest_substring = max(longest_substring, right - left)

    return longest_substring


print(longest_unique_substring("pwwkew"))
