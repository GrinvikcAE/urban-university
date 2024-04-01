
class Build:

    total = 0

    def __init__(self, name):
        self.name = name
        Build.total += 1


for i in range(40):
    build = Build(i)
    print('Build name:', build.name)

print('Total:', Build.total)
