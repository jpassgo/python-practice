
# 
# Given a string s and an integer k, 
# return the length of the longest substring of s that contains at most k distinct characters.
# 
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# 


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    max_substring = float('-inf')
    
    start_window = 0
    end_window = 1

    window_set = {s[start_window], s[end_window]}
    while (end_window < len(s) and start_window < len(s)):
        if len(window_set) > k:
            window_set.remove(s[start_window])
            start_window += 1
            window_set.add(s[start_window])
            break
        
        end_window += 1
        window_set.add(s[end_window])

        if len(window_set) > k:
            max_substring = max(max_substring, start_window + end_window)
            break

    return max_substring


print(lengthOfLongestSubstringKDistinct("eceba", 2))