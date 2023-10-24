l1 = [num for num in range(100)]
l2 = [num for num in range(100)]

# Zips
zip_generator = zip(l1, l2)
for item in zip_generator:
    print(next(zip_generator))

# Maps
cuber = lambda x: x**3

cubed_list = list(map(cuber, [num for num in range(100)]))

print(cubed_list)
