if __name__ == '__main__':
    N = int(input())
    list1= []
    for _ in range(N):
        args = input().split()
        cmd = args[0]
        if cmd == "insert":
            list1.insert(int(args[1]), int(args[2]))
        elif cmd == "print":
            print(list1)
        elif cmd == "remove":
            list1.remove(int(args[1]))
        elif cmd == "append":
            list1.append(int(args[1]))
        elif cmd == "sort":
            list1.sort()
        elif cmd == "pop":
            list1.pop()
        elif cmd == "reverse":
            list1.reverse()
