problems = input().split(";")
ans = 0
for problem in problems:
    if '-' in problem:
        x, y = problem.split("-")
        ans += (int(y) - int(x)) + 1
    else:
        ans += 1
print(ans)
