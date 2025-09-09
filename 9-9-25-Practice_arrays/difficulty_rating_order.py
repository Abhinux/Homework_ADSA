t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    prev=0
    i=0
    while(i<n):
        if d[i]<prev:
            break
        prev=d[i]
        i+=1
    if i<n:
        print("NO")
    else:
        print("YES")