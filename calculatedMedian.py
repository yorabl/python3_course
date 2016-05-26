def median(data):
    length = len(data)

    if (length % 2):
        tmp = (length // 2 )
        middle = sorted(data)[tmp]
    else:
        tmp = length // 2
        middle = (sorted(data)[tmp] + sorted(data)[tmp - 1]) / 2

    return middle


def calc_median():
    l = []
    while True:
        tmp = input('> ')
        if tmp:
            l.append(int(tmp))
        else:
            break
    tmp = 0
    if len(l):
        for i in l:
            tmp += i
        avg = tmp / len(l)

        print('Items: {}'.format(len(l)))
        print('Min: {}'.format(sorted(l)[0]))
        print('Max: {}'.format(sorted(l)[-1]))
        print('Avg: {}'.format(avg))
        print('Median: {}'.format(median(l)))
    else:
        print('You did not enter any number, please try again')


calc_median()