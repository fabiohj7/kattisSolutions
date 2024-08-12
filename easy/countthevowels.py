sen = input()

vowels = "aeiouAEIOU"
counter = 0
for char in sen:
    if char in vowels:
        counter += 1
    else:
        continue
print(counter)
