middle = int(input('Please enter a number between 1-20: '))

for i in range(middle):
    print(' ' * (middle - i) + '*' * ((i * 2) - 1) + ' ' * (middle - i))

for i in range(middle):
    print(' ' * i + '*' * (((middle - i) * 2) - 1) + ' ' * i)
