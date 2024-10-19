n = int(input())

names = {}

for i in range(n):
    fname, lname, classes = input().split()

    name = fname + lname

    if name not in names:
        names[name] = []

    if classes not in names[name]:
        names[name].append(classes)

ans = {}

for value in names.values():
    for i in value:
        if i not in ans:
            ans[i] = 0
        ans[i] += 1

for key in sorted(ans):
    print(f"{key} {ans[key]}")
