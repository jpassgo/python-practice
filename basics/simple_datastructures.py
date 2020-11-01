l = [1, 8, 2, 9, 8, 3, 43]

# Sort without sideaffect
print(sorted(l))
print(l)

# Sort and modify the list
l.sort()
print(l)

# Slicing
print(l[:3])
print(l[3:5])

# List
l = [1, 2, 3, 4, 4, 5]
print(l)

# Set
s = {1, 2, 2, 3, 3, 4, 4, 5}
print(s)

# Dictionary
d = {'one': 1, 'two': 2, 'three': 3}
for key in d.keys():
     print(d[key])