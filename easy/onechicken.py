n, m = map(int, input().split())
diff = abs(n - m)
s = "piece" if diff == 1 else "pieces"
if n > m:
    print(f"Dr. Chaz needs {diff} more {s} of chicken!")
else:
    print(f"Dr. Chaz will have {diff} {s} of chicken left over!")
