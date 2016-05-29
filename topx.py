def find_top_n(n, data):
    """Returns top n numbers as a list, from data (a list of numbers), sorted from highest to lowest"""

    result = []
    for i in range(n):
        result.append(max(data))
        data.pop(data.index(max(data)))

    return result

assert find_top_n(3, [40, 900, 2, 450, 1000, 799, 9]) == [1000, 900, 799]