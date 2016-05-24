num = 0
s = "Please enter the numbers you like to add\n To stop please press enter"
print(s)
while True:
    tmp_num = input("> ")
    if not tmp_num:
        break
    else:
        tmp_num = int(tmp_num)
        num += tmp_num

print("{}".format(num))