immutable_var = (0, True, 'str', 1.5, [0, 5, False], {0, 3, 5, 3, 3})
print(immutable_var)

try:
    immutable_var[1] = False
    print(immutable_var)
except Exception as e:
    print(f'Explanation: {e}')


mutable_list = [0, True, 'str', 1.5, [0, 5, False], {0, 3, 5, 3, 3}]
mutable_list[1] = False
print(mutable_list)
