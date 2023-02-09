print("", "1", "2", "3", sep = "     ")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"1 {row1}\n2 {row2}\n3 {row3}")

position = input("Where do you want to put the treasure? First number is row. ")

map[int(position[0]) - 1][int(position[1]) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")