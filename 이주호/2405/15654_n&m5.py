n, m = map(int, input().split())
array1 = sorted(list(map(int, input().split())))
arr = []
visited = [0 for _ in range(n+1)]


def recur(number):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(0, n):
        if visited[i+1]==1:
            continue

        visited[i+1]=1

        arr.append(array1[i])
        recur(array1[i])
        arr.pop()
        visited[i+1]=0

recur(array1[0])

