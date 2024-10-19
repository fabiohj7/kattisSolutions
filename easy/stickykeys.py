s = input().split()
for word in s:
    ans = ''
    i = 0
    for letter in word:
        if ans == '':
            ans += letter
            continue
        if word[i] == letter:
            i += 1
            continue
        ans += letter
        i += 1
    print(ans, end=' ')
print()
