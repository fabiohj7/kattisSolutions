x = int(input())
queue = list(input())
men = 0
women = 0
i = 0

while i < len(queue):
    if queue[i] == "M":
        if abs(men + 1 - women) > x:
            if i != (len(queue) - 1) and queue[i + 1] == 'W':
                women += 1
                queue[i + 1] = 'M'
            else:
                break
        else:
            men += 1
    if queue[i] == "W":
        if abs(women + 1 - men) > x:
            if i != len(queue) - 1 and queue[i + 1] == 'M':
                men += 1
                queue[i + 1] = 'W'
            else:
                break
        else:
            women += 1
    # print(queue)
    # print(f"Women: {women} Men: {men}")

    i += 1
print(women + men)
