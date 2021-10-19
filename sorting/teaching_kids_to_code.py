adjectives = {1: 'smart', 2: 'fast', 3: 'big', 4: 'poisonous'}

animal = input('What animal are you describing? ')

inputs = [input(f'Is a {animal} {adjectives.get(i)}? ') for i in range(1, len(adjectives) + 1)]

[print(f'A {animal} is {adjectives.get(i)}') for i in range(1, len(inputs) + 1) if inputs[i-1] == 'yes']
