n = int(input())

for i in range(n):
    r, e, c = [int(x) for x in input().split()]
    e = e - c
    if r > e:
        print("do not advertise")
    elif e > r:
        print("advertise")
    else:
        print("does not matter")
