
def test() -> None:
    a = 1
    b = True
    print(a, b, sep='\n')


def test2(arg1, arg2, arg3) -> None:
    print(arg1, arg2, arg3, sep='\n')


test()
print()
test2(2.5, 'hello', ['world', False, None])
