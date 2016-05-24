first_num = 0
second_num = 1
magic_num = 10000

print(second_num)
while (second_num + first_num) < magic_num:
    print('{}'.format(second_num + first_num))
    tmp = second_num
    second_num += first_num
    first_num = tmp
