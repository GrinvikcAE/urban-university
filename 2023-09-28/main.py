# first, second, third = map(int, input().split())
first, second, third = int(input()), int(input()), int(input())

check = {first, second, third}
match len(check):
    case 3:
        print(0)
    case 2:
        print(2)
    case 1:
        print(3)
