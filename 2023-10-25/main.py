

class House:
    def __init__(self):
        self.number_of_floors = 10


house = House()
for i in range(1, house.number_of_floors + 1):
    print(f'Текущий этаж равен: {i}')