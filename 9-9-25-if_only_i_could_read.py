t = int(input()) 

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res=[]
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            res=[i+1,i+2] 
            found = True
            break

    if res!=[]:
        print(res[0],res[1])
    else:

        print(-1)
