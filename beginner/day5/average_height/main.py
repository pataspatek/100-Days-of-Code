student_heights = input("Input a list of student heights: ").split()

sum = 0
student_count = 0

for i in student_heights:
    sum += int(i)
    student_count += 1

avarage = round(sum / student_count)
print(avarage)

