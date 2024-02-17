
x = 38

print('Hello')

if x < 0:
    print('Is negative number')

print('Goodbye')

a, b = 5, 10

if a > b:
    print('a > b')
if a > b and a > 0:
    print('1. Great')
if a > b and (a > 0 or b < 1000):
    print('2. Great')
if 5 < b < 10:
    print('3. Great')

if '34' > '123':
    print('4. Great')
if '123' > '12':
    print('5. Great')
if [1, 2] > [1, 1]:
    print('6. Great')

try:
    if '6' > 5:
        print('7. Great')

except TypeError as err:
    print(err)
try:
    if [5, 6] > 5:
        print('8. Great')
except TypeError as err:
    print(err)

if '6' != 5:
    print('9. Great')
