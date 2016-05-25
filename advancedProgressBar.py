def advanced_progress_bar(width, total, completed):
    # --------- YOUR CODE HERE --------------
    ratio = (completed / total)

    tags = width * ratio
    tags = int(tags)
    str = '|' + '#' * tags + '-' * (width - tags) + '|' '{}%'.format(int(ratio * 100))
    print('{} {} '.format(tags, ratio))
    return str
    # --------- YOUR CODE HERE --------------


print()
print()

print(advanced_progress_bar(20, 5, 0))
print(advanced_progress_bar(20, 5, 1))
print(advanced_progress_bar(20, 5, 2))
print(advanced_progress_bar(20, 5, 3))
print(advanced_progress_bar(20, 5, 4))
print(advanced_progress_bar(20, 5, 5))

print()
print("OK!")