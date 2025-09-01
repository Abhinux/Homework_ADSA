n=int(input())
for i in range(n):
    s=int(input())
    res=''
    char=['a','b','c']
    for j in range(s):
        res+=char[j%3]
    print(res)