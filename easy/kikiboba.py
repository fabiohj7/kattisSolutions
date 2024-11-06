s = input()
k = 0
b = 0
for i in s:
    if i == "k":
        k += 1
    elif i == "b":
        b += 1

if k > b:
    print("kiki")
elif k < b:
    print("boba")
elif k == 0 and b == 0:
    print("none")
elif k == b:
    print("boki")
