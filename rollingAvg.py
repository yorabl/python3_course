def rolling_average(l, window):
    result_list = []
    for i in range(len(l) - window + 1):
        tmp = 0
        for j in l[i:i + window]:
            tmp += j

        result_list.append(tmp / window)

    return result_list

assert [2.0, 3.0, 4.0, 5.0] == rolling_average([1, 2, 3, 4, 5, 6], 3)
assert [5.0] == rolling_average([0, 10], 2)
assert [5.0, 12.5] == rolling_average([0, 10, 15], 2)
assert [18.25, 15.75] == rolling_average([10, 10, 22, 31, 0], 4)