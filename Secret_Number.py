n=int(input())
for i in range(n):
    y=int(input())
    res=[]
    m=1
    denominator=11  # 10**1+1 = 11
    while(denominator<=y):
        if y%denominator==0:
            res.append(str(y//denominator))
        m+=1
        denominator=(10**m)+1
    if res:
        print(len(res))
        print(" ".join(reversed(res)))
    else:
        print(0)
        