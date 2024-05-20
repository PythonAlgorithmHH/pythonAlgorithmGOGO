a,b=map(int,input().split())
tmp_a=0
tmp_b=0
tmp_a +=a
tmp_b +=b
for i in range(2,50):
    tmp_a+=(a//(2**i))*(2**i - 2**(i-1))
    tmp_b+=(b//(2**i))*(2**i - 2**(i-1))
print(tmp_a - tmp_b)