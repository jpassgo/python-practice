import re

pattern = '[a-zA-Z0-9]+@[a-zA-z]+\.(com|org|net)'

user_input = input()

print('Valid Email') if re.search(pattern, user_input) else print('Invalid Email')

