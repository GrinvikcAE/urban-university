grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = frozenset(students)
dct_std = {std: (sum(grd)/len(grd)) for std, grd in zip(students, grades)}
print(dct_std)