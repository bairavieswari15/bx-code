if __name__ == '__main__':
    n = int(raw_input())
    list1 = map(int, raw_input().split())
    t = tuple(list1)
    print hash(t)
