
def multiply_up_to_n(n):     
    return [(x+1)*(x+1) for x in range(n)]


def coordinates_from_two_ranges(i, j):
    for x, y in zip(range(i), range(j)):
        print(f"x={x},y={y}")



print(multiply_up_to_n(5))

print(coordinates_from_two_ranges(2,12))