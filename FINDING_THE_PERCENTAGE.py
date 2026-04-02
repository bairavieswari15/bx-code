if __name__ == '__main__':
    n=int(input())
    studmarks={}
    for _ in range(n):
        line=input().split()
        name=line[0]
        scores=[float(x) for x in line[1:]]
        studmarks[name]=scores
name2=input()
marks=studmarks[name2]
average=sum(marks)/len(marks)
print(f"{average:.2f}")        
