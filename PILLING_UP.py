from collections import deque
def solve():
    n = int(input())
    cubes = deque(map(int, input().split()))
    lastpicked = float('inf')
    possible = True
    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()
        if current > lastpicked:
            possible = False
            break
        lastpicked = current
    print("Yes" if possible else "No")
t = int(input())
for _ in range(t):
    solve()
