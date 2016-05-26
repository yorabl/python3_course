def median(data):
    length = len(data)

    if (length % 2):
        tmp = (length // 2 )
        middle = sorted(data)[tmp]
    else:
        tmp = length // 2
        middle = (sorted(data)[tmp] + sorted(data)[tmp - 1]) / 2

    return middle



result = median([10, 15, 20, -40, 90])
print(result)
assert result == 15

result = median([10, 15, 20, -40, 90, 33])
print(result)
assert result == 17.5

print("OK")