t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    a=sorted(list(set(a)))
    print(a[-1]+a[-2])