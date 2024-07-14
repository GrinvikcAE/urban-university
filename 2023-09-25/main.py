my_dict = {1: 'one', 2: 'two', 3: 'three', 4: ''}

print(my_dict)
print(my_dict[1])
print(my_dict.get(123))

my_dict[5] = 'five'
my_dict[6] = 'six'

print(my_dict.pop(2))
print()

my_set = {1, 2, True, 1, 1.1, False, 'abc', (0, 1, 2)}
print(my_set)
my_set.add((0, 1))
my_set.add(my_dict.values())
my_set.discard(True)
print(my_set)
