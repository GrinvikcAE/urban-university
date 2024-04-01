class Build:

    def __init__(self, number_of_floors, building_type):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and \
            self.building_type == other.building_type


build_1 = Build(10, 'Electrical')

build_2 = Build(10, 'Electrical')

build_3 = Build(5, 'Home')

build_4 = Build(5, 'Electrical')

print(build_1 == build_2)
print(build_1 == build_3)
print(build_2 == build_3)
print(build_3 == build_4)
print(build_1 == build_2 == build_3)
