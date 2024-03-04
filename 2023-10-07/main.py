
def print_params(a=1, b='string', c=True) -> None:
    print(a, b, c, sep='\n')


print_params()
print()

print_params('this is not')
print()

print_params(b=25)
print()

print_params(c=[1,2,3])
print()

print_params(a=True, c=25)
print()


value_list = [1.05, 'this is string', False]
print_params(*value_list)
print()

value_dict = {'a': 1245, 'b': None, 'c': False}
print_params(**value_dict)
print()

value_list_2 = [1.005, 'this is a new string']
print_params(*value_list_2, 42)
