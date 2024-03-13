

def test_function() -> None:

    def inner_function() -> None:
        print('Я в области видимости функции test_function')

    inner_function()


try:
    inner_function()
except Exception as e:
    print(e)

test_function()
