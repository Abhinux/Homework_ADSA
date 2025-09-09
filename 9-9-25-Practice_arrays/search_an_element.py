n,x=input().split(" ")
n=int(n)
l=list(input().split(" "))
i=0
res="NO"
while(i<n):
    if x==l[i]:
        res="YES"
        break
    i+=1
print(res)