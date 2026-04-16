from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
combos = list(combinations(range(n), k))
favorable = [c for c in combos if any(letters[i] == 'a' for i in c)]
print(f"{len(favorable) / len(combos):.4f}")
