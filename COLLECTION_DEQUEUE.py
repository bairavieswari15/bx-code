from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    line = input().split()
    command = line[0]
    if len(line) > 1:
        getattr(d, command)(line[1])
    else:
        getattr(d, command)()
print(*(d))
