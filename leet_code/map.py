this_list = [1, 2, 3, 4]

even_numbers = map(lambda x: x % 2, this_list)

print(list(even_numbers))


my_lambda = lambda x, y: x + y

my_dictionary = {1: 2, 2: 3, 3: 4}

map(
    my_lambda,
)
