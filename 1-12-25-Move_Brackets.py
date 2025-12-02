q=int(input())
for _ in range(q):
    n=int(input())
    brack=input()
    stck=[]
    res=0
    for i in brack:
        if i==")" and stck==[]:
            res+=1
        else:
            if i=="(":
                stck.append(i)
            else:
                stck.pop()
    print(res)