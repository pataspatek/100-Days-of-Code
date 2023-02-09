import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need {num_of_cans} cans of paint.")

height_wall = int(input("Height of wall: "))
width_wall = int(input("Width of wall: "))
coverage = 5

paint_calc(height_wall, width_wall, coverage)