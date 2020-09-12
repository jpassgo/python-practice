import random
import demos

def create_ran_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1, max_val))
    return ran_list

size = int(input("What size list do you want to create?"))
max_value = int(input("What is the max value of the range?"))

l = create_ran_list(size, max_value)

print(f"Unsorted: \n {l}")
print(f"Sorted: \n {demos.quicksort(l)}")