import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

pick_name = random.randint(0, len(names) - 1)

print(names[pick_name])