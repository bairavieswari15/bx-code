import sys
if __name__ == '__main__':
    line1 = sys.stdin.readline()
    if not line1:
        sys.exit()
    k = int(line1.strip())
    line2 = sys.stdin.readline()
    if not line2:
        sys.exit()
    roomlist = list(map(int, line2.split()))
    counts = {}
    for room in roomlist:
        counts[room] = counts.get(room, 0) + 1
    for room, count in counts.items():
        if count == 1:
            print(room)
            break
