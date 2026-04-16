from itertools import groupby
s = input().strip()
result = []
for k, g in groupby(s):
    count = len(list(g))
    result.append(f"({count}, {k})")
print(" ".join(result))
