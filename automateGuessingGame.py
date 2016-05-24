print("Please choose a number between 1-100")

high = 100
low = 1
num = (low + high) // 2
is_right = 'n'
num_status = 'n'

while True:
    is_right = input('Is it {}? [y/n]'.format(num))
    if is_right is 'y':
        break
    num_status = input('Is the number {} is too high?[y/n]'.format(num))
    if num_status is 'y':
        high = num - 1
    elif num_status is 'n':
        low = num + 1
    num = (high + low) // 2

print('Great! the number is {}'.format(num))


