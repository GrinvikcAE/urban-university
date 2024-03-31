

class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_number_of_floors(self, floors):
        self.number_of_floors = floors
        print(f'Current number of floors: {self.number_of_floors}')


house = House()
print(f'Current number of floors: {house.number_of_floors}')
house.set_number_of_floors(5)
