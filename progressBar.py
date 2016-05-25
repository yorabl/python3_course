def progress_bar(width, total, completed):
    """Returns a progress bar as str of width width
    composed of the characters '#' for the completed part
    and '-' for the uncompleted part"""
    # --------- YOUR CODE HERE --------------
    ratio = (completed / total)

    tags = width * ratio
    tags = int(tags)
    s = '#' * tags + '-' * (width - tags)
    print('{} {} '.format(tags, ratio))
    return s
    # --------- YOUR CODE HERE --------------


result = progress_bar(10, 100, 32)
print(result)
assert result == "###-------"

result = progress_bar(20, 10, 4)
print(result)
assert result == "########------------"

result = progress_bar(8, 1000, 260)
print(result)
assert result == "##------"

result = progress_bar(12, 85, 85)
print(result)
assert result == "############"

print()
print()

print(progress_bar(20, 5, 0))
print(progress_bar(20, 5, 1))
print(progress_bar(20, 5, 2))
print(progress_bar(20, 5, 3))
print(progress_bar(20, 5, 4))
print(progress_bar(20, 5, 5))

print("OK!")