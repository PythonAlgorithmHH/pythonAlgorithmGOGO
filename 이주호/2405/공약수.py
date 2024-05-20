import sys
input = sys.stdin.readline
n, m = map(int, input().split())

"""
a,b =36,30
tmp=0
while b != 1:
    tmp=b
    a=b
    b=a%b
print(tmp)    

"""
div = m//n
inf = 20000000
def gcd(a,b):
    if a%b==0:return b
    return gcd(b,a%b)
for a in range(1,int((div**0.5)+1)):
    b=int(div/a)
    if div%a==0 and gcd(a,b)==1:
        answer= f'{a*n} {b*n}'
print(answer)
