n=int(input())
arr=list(map(int,input().split(" ")))
x=0
res=1
for i in range(1,n):
    same=False
    
    for j in range(x,i):
        if arr[j]==arr[i]:
            x=j+1
            same=True
            break
    curr_res=i-x+1
    if same==False and curr_res>res:
        res=curr_res
print(res)
