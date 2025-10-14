n=int(input())
for i in range(n):
    S1=input()
    lower=[]
    upper=[]
    res=[""]*len(S1)
    for j in range(len(S1)):
        letter=S1[j]
        if letter=="b":
            if lower:
                lower.pop()
        elif letter=="B":
            if upper:
                upper.pop()
        elif letter.isupper():
            upper.append(j)
        elif letter.islower():
            lower.append(j)
    for k in lower:
        res[k]=S1[k]
    for k in upper:
        res[k]=S1[k]
    print("".join(res))
    
        
