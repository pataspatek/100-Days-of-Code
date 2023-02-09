student_scores = input("Input a list of student scores: ").split()

maximum = 0
for i in student_scores:
    i = int(i)
    if i > maximum:
        maximum = i
print(f"The highest score in the class is: {maximum}")
