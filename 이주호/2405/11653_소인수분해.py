# import sys
# input = sys.stdin.readline
# n=int(input())
# while n != 1:
#     for i in range(2,10000000):
#         if (n%i==0):
#             n=n//i
#             print(i)
#             break
n=int(input())
i=2
while i*i<=n:
    while n%i==0:
        n//=i
        print(i)
    i+=1
if n>1:
    print(n)