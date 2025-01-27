cups = input()
pos = [1, 0, 0]
for i in cups:
    if i == 'A':
        pos[0], pos[1] = pos[1], pos[0]
    elif i == 'B':
        pos[1], pos[2] = pos[2], pos[1]
    else:
        pos[0], pos[2] = pos[2], pos[0]

for i in range(len(pos)):
    if pos[i] == 1:
        print(i + 1)
        break
