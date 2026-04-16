from itertools import permutations
s, k = input().split()
k = int(k)
result = list(permutations(sorted(s), k))
for p in result:
    print("".join(p))
