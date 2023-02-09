height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

bmi = weight/height ** 2
result = int(bmi)

print(f"Your BMI is {result}")