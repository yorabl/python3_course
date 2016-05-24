# father1.py
name = "joe"
sons = 2
daughters = 3

# ----- ENTER YOUR CODE HERE --------
s = "{} has {} kids.".format(name.capitalize(), sons + daughters)
# -----------------------------------

print(s)
assert s == "Joe has 5 kids."
print("OK")

name = input("What is your name? ")
sons = int(input("How many sons do you have? "))
daughters = int(input("How many daughters do you have? "))

s = "{} has {} kids.".format(name.capitalize(), sons + daughters)

print(s)