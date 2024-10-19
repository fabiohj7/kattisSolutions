detected = False
for i in range(5):
    codes = input()
    if "FBI" in codes:
        print(i + 1, end=' ')
        detected = True

if not detected:
    print("HE GOT AWAY!")
