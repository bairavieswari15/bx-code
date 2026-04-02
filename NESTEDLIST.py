if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(list(set([s[1] for s in students])))
    slg= scores[1]
    runners = [s[0] for s in students if s[1] == slg]
    runners.sort()
    for name in runners:
        print(name)
