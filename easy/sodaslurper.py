e, f, c = [int(x) for x in input().split()]

e = e + f
remainder = 0
ans = 0
while e >= c:
    temp = e // c
    remainder += temp % c
    e = temp
    ans += temp
if (remainder + e) >= c:
    e += remainder
    ans += e // c
print(ans)
