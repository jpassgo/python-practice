# 
# 10. Regular Expression Matching
# 
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# 
# https://leetcode.com/problems/regular-expression-matching/
# 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ops = []
        sub_pattern = ''
        for character in p:
            if character == '.' or character == '*':
                ops.append(sub_pattern)
                sub_pattern = ''
                ops.append(character)
            else:
                sub_pattern = sub_pattern + character

        op_index = 0
        s_index = 0
        s_len = len(s)  
        matches = True
        prev = ''
        while matches and s_index < s_len:            
            op = ops[op_index]   
            op_len = len(op)         
            if op == '.':
                op_index += 1
                s_index += 1
                return
            elif op == '*':
                while s[s_index] == op[op_index-1][len(op[op_index-1])]:                    
                    s_index += 1
            elif op_len > 0:
                i
                while 


        