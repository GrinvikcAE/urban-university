
lst = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = lst[0]
i = 0
l = len(lst)

while num >= 0:
    if num != 0:
        print(num)
    i += 1
    if i >= l:
        break
    num = lst[i]
