import math
n=int(input())
for i in range(n):
    y=int(input())
    res=[]
    k=1
    denominator=11 # 10**1+1 = 11
    while(denominator<y):
        x=y/denominator
        if math.floor(x)==x:
            res.append(str(math.floor(x)))
        k+=1
        denominator=(10**k)+1
    if res:
        r=len(res)
        print(r)
        print(" ".join(res))
    else:
        print(0)

