seats = input()
seats = seats.split()

group = input()
groups = group.split()

space = 0
num = 0
for g in groups:
    space += int(g)
    if space > int(seats[0]):
        result = int(seats[1]) - num
        break
    num += 1

print(result)
