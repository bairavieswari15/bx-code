from collections import Counter
if __name__ == '__main__':
    s = input().strip()  
    counts = Counter(s)
    sortedchars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for i in range(3):
        print(f"{sortedchars[i][0]} {sortedchars[i][1]}")
