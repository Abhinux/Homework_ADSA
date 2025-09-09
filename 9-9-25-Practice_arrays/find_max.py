t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split()))
    Max=array[0]
    j=1
    while(j<n):
        if array[j]>Max:
            Max=array[j]
        j+=1
    print(Max)
    