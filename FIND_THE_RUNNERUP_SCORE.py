if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = sorted(list(set(arr)))
    print(scores[-2])
