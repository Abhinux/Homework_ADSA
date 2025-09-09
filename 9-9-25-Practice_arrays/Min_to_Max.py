t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    m=min(a)
    print(n-a.count(m))