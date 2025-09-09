t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    total=0
    discounted=x
    for i in a:
        if i>y:
            discounted+=i-y
        total+=i
    if total>discounted:
        print("COUPON")
    else:
        print("NO COUPON")
