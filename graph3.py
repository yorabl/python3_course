def graph(data):
    for i in data:
        print('{:>15}\t|{}'.format(i[0], '=' * i[1]))

data = [
    ['January', 5],
    ['February', 20],
    ['March', 16],
    ['April', 3],
    ['May', 7],
    ['June', 7],
    ['July', 19],
    ['August', 6],
    ['September', 3],
    ['October', 8],
    ['November', 3],
    ['December', 19],
]

graph(data)