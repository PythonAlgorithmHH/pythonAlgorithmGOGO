import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
tmp=[]
def bt(start):
    if len(tmp)==m:
        print(*tmp)
        return
    for i in range(start,n):
        tmp.append(i)
        bt(i)
        tmp.pop()
bt(0)