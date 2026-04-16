from itertools import combinations_with_replacement
s, k = input().split()
k = int(k)
s_sorted = sorted(s)
for combo in combinations_with_replacement(s_sorted, k):
    print("".join(combo))
