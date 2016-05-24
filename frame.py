while True:
    num = int(input("Please enter a number between 1-100: "))
    if 0 < num < 101:
        break

for i in range(num):
    if 0 < i < (num -1) :
        print('*' + ' ' * (num - 2) + '*')
    else:
        print('*' * num)
