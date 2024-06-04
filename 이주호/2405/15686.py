n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

home=[]
chic=[]
for i in range(n):
    for j in range(n):
        if row[j]==1:
            home.append([i,j])
        elif row[j]==2:
            chic.append([i,j])
visited=[0]*len(chic)
min_ans=999999999
def dfs(idx,cnt):
    global min_ans
    if cnt == m:
        ans=0
        for i in home:
            distance=99999999
            for j in range(len(chic)):
                if visited[j]:
                    check_num=abs(i[0]-chic[j][0])+abs(i[1]-chic[j][1])
                    distance=min(distance,check_num)
            ans+=distance
        min_answ=min(ans,min_ans)
        return
    for i in range(idx,len(chic)):
        if not visited[i]:
            visited[i]=True
            dfs(idx+1,cnt+1)
            visited[i]=False
dfs(0,0)
print(min_ans)