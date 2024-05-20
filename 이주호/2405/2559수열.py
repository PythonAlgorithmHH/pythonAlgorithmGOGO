n,k=map(int,input().split())
arr=list(map(int,input().split()))
answer=[]
prefix = [0 for _ in range(n+1)]
for i in range(n):
    prefix[i+1] = prefix[i]+arr[i]
for i in range(k,n):
    answer.append(prefix[i]-prefix[i-k])
print(max(answer))