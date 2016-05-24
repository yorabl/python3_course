p1_num = 0
p2_num = 0

while p1_num < 1 or p1_num > 100:
    p1_num = int(input("Please enter a number between 1 - 100: "))

print("\n" * 100)

while True:
    p2_num = int(input("Please guess a number, between 1-100: "))
    if p2_num < p1_num:
        print("Your guess, {}, is too low!".format(p2_num))
    elif p2_num > p1_num:
        print("Your guess, {} is too high!".format(p2_num))
    else:
        print("You are correct!")
        break