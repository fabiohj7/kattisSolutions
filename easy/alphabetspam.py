s = input()
upper = 0
lower = 0
white = 0
symbols = 0
n = len(s)

for i in s:
    if 33 <= ord(i) <= 64 or 91 <= ord(i) <= 94 or ord(
            i) == 96 or 123 <= ord(i) <= 126:
        symbols += 1
    elif 65 <= ord(i) <= 90:
        upper += 1
    elif 97 <= ord(i) <= 122:
        lower += 1
    elif i == "_":
        white += 1

print(white / n)
print(lower / n)
print(upper / n)
print(symbols / n)
