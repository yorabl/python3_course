def bin2dec(s):
    """
    string -> int

    Converts a binary number represented as a string of 0s and 1s
    to a decimal number
    """
    num = 0
    length = len(s)

    for i in range(length):
        tmp_num = int(s[length - i - 1])
        tmp_num *= 2 ** i

        num += tmp_num
    print(num)

    return num



bin2dec('1001')
assert 7 == bin2dec('111')
assert 21 == bin2dec('10101')
assert 4 == bin2dec('100')
assert 255 == bin2dec('11111111')
assert 73 == bin2dec('1001001')