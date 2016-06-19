def funny(s):
    # === YOUR CODE HERE! ===

    return ' '.join([i[::-1].capitalize() for i in s.split()])
    # =======================


result = funny("Foo bar")
print(result)
assert result == "Oof Rab"

result = funny("The quick brown fox")
print(result)
assert result == "Eht Kciuq Nworb Xof"

print("OK")