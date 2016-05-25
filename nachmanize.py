def nachmanize(str):
    tmp_list = []
    for i in range(len(str) + 1):
        tmp_list.append(''.join(str[:i]))
    tmp_list.pop(0)

    return ' '.join(tmp_list)


result = nachmanize("abcd")
print(result)
assert result == "a ab abc abcd"

result = nachmanize("shalom")
print(result)
assert result == "s sh sha shal shalo shalom"

print("OK")
