# Secret Name Guess!
name = input("Guess the jolly secret name?: ")
name = name.upper()
names_collect = []

while name != "SANTA":
    names_collect.append(name)
    name = input("Take a festive guess: Who am I? (Hint: Think December, Snow, and Gifts!: ")
    name = name.upper()

print(f"--------\nBravo!! Well played and holiday cheers!\nHere's your guessing journey:")
for x in names_collect:
    print(x)