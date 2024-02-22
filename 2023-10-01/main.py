from typing import Any


def print_params(arg_1: Any) -> None:
    for _ in range(2):
        print(arg_1)


print_params("I believe in miracles")
print_params(666)
