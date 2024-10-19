n, p = [int(x) for x in input().split()]

grades = [int(x) for x in input().split()]


def get_average(grades):
    return sum(grades) // len(grades)


total = get_average(grades)
counter = 0

if p == 100 and total != 100:
    print("impossible")
    exit()

while total < p:
    grades.append(100)
    total = get_average(grades)
    counter += 1

print(counter)
