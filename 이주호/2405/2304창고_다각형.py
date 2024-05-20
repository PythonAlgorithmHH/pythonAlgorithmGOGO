import sys
input =sys.stdin.readline

n=int(input())
arr=[[list(map(int,input().split()))] for _ in range(n)]
arr.sort()
print(arr)

answer=0
for i in range(arr[1][0],arr[-1][0]):
    answer+=i[1]
print(answer)
