def get_multiplied_digits(number):
    s_number = str(number)
    if len(s_number) == 1:
        return number
    first = int(s_number[0])
    return first * get_multiplied_digits(int(s_number[1:]))


result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(123)
print(result)

result = get_multiplied_digits(4321)
print(result)
