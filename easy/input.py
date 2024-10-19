import random

f = open("input.txt", 'w')

n = random.randint(0, 30)

grades = []
for i in range(n):
    temp = random.randint(0, 100)
    grades.append(temp)

total = 0
for grade in grades:
    total += grade

total = total // n

p = random.randint(total, 100)

grades_str = " ".join(str(i) for i in grades)

f.write(f"{n} {p}\n{grades_str}")
