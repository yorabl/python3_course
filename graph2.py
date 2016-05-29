def graph(data):

    for i in data:
        if i == max(data):
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