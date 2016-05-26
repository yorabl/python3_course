def graph(data):
    max_num = 0
    for i in data:
        if i > max_num:
            max_num = i
    for i in data:
        if i == max_num:
            print('*' * i)
        else:
            print('=' * i)

data = [
    10,
    3,
    2,
    16,
    8,
    3,
    7,
    9,
    12,
    16,
    0,
    4,
    10,
]

graph(data)