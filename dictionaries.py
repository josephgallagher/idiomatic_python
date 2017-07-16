__author__ = 'joseph'
from collections import defaultdict

names = ['rachel', 'robert', 'randy', 'joseph', 'meghan', 'meryl', 'andrew', 'thomas', 'eric', 'matt', 'melissa', 'benjamin']
colors = ['red', 'green', 'green', 'blue', 'green', 'red', 'orange', 'green', 'red', 'yellow', 'orange']
d = {'a': 1, 'b': 2, 'c': 1, 'd': 34, 'e': -11, 'f': 123}


# Iterating over dict:
for k, v in d.items():
    print(k, ' --> ', v)

# Construct dict from list with keys as their list indices:
new_dict = dict(enumerate(names))
print(new_dict)

# Constructing a dict from two lists:
new_dict = dict(zip(names, colors))
print("Constructing dict from 2 lists with zip():", new_dict)

# Counting with dictionaries, naive:
c = {}
for color in colors:
    if color not in c:
        c[color] = 0
    c[color] += 1
print("Counting naively:", c)

# Counting using get:
c = {}
for color in colors:
    c[color] = c.get(color, 0) + 1
print("Counting using dict.get():", c)

# Counting with defaultdict:
c = defaultdict(int)
for color in colors:
    c[color] += 1
print("Counting with defaultdict:", c)

# Grouping with dictionaries:
new_dict = {}
for name in names:
    key = len(name)
    if key not in new_dict:
        new_dict[key] = []
    new_dict[key].append(name)
print("Grouping naive: ", new_dict)

# Grouping with setdefault:
new_dict = {}
for name in names:
    key = len(name)
    new_dict.setdefault(key, []).append(name)
print("Grouping with setdefault: ", new_dict)

# Grouping with defaultdict:
new_dict = defaultdict(list)
for name in names:
    key = len(name)
    new_dict[key].append(name)
print("Grouping with defaultdict: ", new_dict)