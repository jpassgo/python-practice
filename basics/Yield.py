l1 = [num for num in range(1, 100)]

def yield_my_map(function, iterable):
    for item in iterable:
        yield(function(item))

def my_map(function, iterable):
    return (function(item) for item in iterable)

print(list(yield_my_map(lambda x: x**2, l1)))
print(list(my_map(lambda x: x**2, l1)))

