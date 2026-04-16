from collections import defaultdict
n, m = map(int, input().split())
group_a = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    group_a[word].append(str(i))
for _ in range(m):
    word_b = input()
    if word_b in group_a:
        print(" ".join(group_a[word_b]))
    else:
        print("-1")
