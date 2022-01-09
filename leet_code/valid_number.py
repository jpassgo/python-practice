# 65. Valid Number
# 
# A valid number can be split up into these components (in order):
# 1. A decimal number or an integer.
# 2. (Optional) An 'e' or 'E', followed by an integer.
#  
# A decimal number can be split up into these components (in order):
# 1. (Optional) A sign character (either '+' or '-').
# 2. One of the following formats:
#   1. One or more digits, followed by a dot '.'.
#   2. One or more digits, followed by a dot '.', followed by one or more digits.
#   3. A dot '.', followed by one or more digits.
#
#  An integer can be split up into these components (in order):
#  1. (Optional) A sign character (either '+' or '-').
#  2. One or more digits.
# 
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
# 
# Given a string s, return true if s is a valid number.
# 
# https://leetcode.com/problems/valid-number/
# 




def isNumber(s: str) -> bool:
    operand_allowed = True
    digit_allowed = True
    e_allowed = False
    dot_allowed = False

    e_allowed_override = True
    dot_allowed_override = True

    if s[len(s)-1].lower() == 'e' or s[0].lower() == 'e':
        return False
    
    for character in s:
        character_type = determine_character_type(character)
        invalid_number = False
        if character_type == 'INVALID':
            return False
        elif character_type == 'DIGIT' and digit_allowed:
            e_allowed = True
            dot_allowed = True   
            invalid_number = True                
            pass
        elif character_type == 'operand' and operand_allowed:
            operand_allowed = False
            e_allowed = False
            dot_allowed = True
            invalid_number = True
            pass
        elif character_type == 'DOT' and dot_allowed and dot_allowed_override:
            digit_allowed = True
            operand_allowed = False
            e_allowed = False
            dot_allowed = False  
            invalid_number = True          
            pass
        elif character_type == 'E' and e_allowed:
            digit_allowed = True
            operand_allowed = True
            dot_allowed_override = False
            e_allowed_override = False
            invalid_number = True
            pass   


    return invalid_number

def determine_character_type(c):
    if c.isdigit():
        return 'DIGIT'
    elif c == '-' or c == '+':
        return 'OPERAND'
    elif c == '.':
        return 'DOT'
    elif c.lower() == 'e':
        return 'E'
    else:
        return 'INVALID'

# valid
# print('valid')
# print(isNumber('2'))
# print(isNumber('0089'))
# print(isNumber('-0.1'))
# print(isNumber('+3.14'))
# print(isNumber('4.'))
# print(isNumber('-.9'))
# print(isNumber('2e10'))
# print(isNumber('-90E3'))
# print(isNumber('3e+7'))
# print(isNumber('+6e-1'))

# invalid
print('invalid')
print(isNumber('abc'))
print(isNumber('1a'))
print(isNumber('1e'))
print(isNumber('e3'))
print(isNumber('99e2.5'))
print(isNumber('1a'))
print(isNumber('1a'))