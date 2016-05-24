height = int(input('Please enter the number height of the pyramid: '))

for i in range(height):
    print(' ' * (height - i) + '*' * ((i * 2) - 1) + ' ' * (height - i))