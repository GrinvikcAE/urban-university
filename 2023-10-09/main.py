from math import factorial as fct


def test(*args) -> None:
    print(*args, sep=', ')


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)


test(1, 2, 3, 4, 5, 6, 7, 8, 9)
test(1, 2, 3, 4, 5, 6, 7, 8)
test('a', [1, 2, 3, 4, 5, 6, 7, 8, 9], {'a': 1, 'b': 2})


assert factorial(2) == fct(2)
assert factorial(8) == fct(8)
assert factorial(10) == fct(10)

test(factorial(5))
