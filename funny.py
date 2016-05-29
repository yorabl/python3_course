def funny(s):
    # === YOUR CODE HERE! ===
    l = s[::-1].split()
    l2 = []
    [l2.append(i.capitalize()) for i in l]
    l2.reverse()
    return ' '.join(l2)
    # =======================


result = funny("Foo bar")
print(result)
assert result == "Oof Rab"

result = funny("The quick brown fox")
print(result)
assert result == "Eht Kciuq Nworb Xof"

print("OK")