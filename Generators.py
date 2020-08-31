l1 = [num for num in range(100)]
l2 = [num for num in range(100)]

zip_generator = zip(l1, l2)

cuber = lambda x: x**3

cubed_list = list(map(cuber, [num for num in range(100)]))

print(cubed_list)