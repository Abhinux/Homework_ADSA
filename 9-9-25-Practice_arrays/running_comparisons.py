t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    i=0
    res=0
    while(i<n):
        if a[i]<=2*b[i] and 2*a[i]>=b[i]:
            res+=1
        i+=1
    print(res)