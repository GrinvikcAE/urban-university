from typing import Any


def get_matrix(
        n: int = 0,
        m: int = 0,
        values: Any = None
) -> list[list[Any]]:
    matrix = []
    for _ in range(n):
        matrix.append([values] * m)

    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

result_zero = get_matrix(2, 0, 10)
print(result_zero)

result_zero = get_matrix(0, 0, 10)
print(result_zero)

result_zero = get_matrix(2, -1, 10)
print(result_zero)
