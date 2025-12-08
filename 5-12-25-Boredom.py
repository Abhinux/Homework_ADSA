import sys
sys.setrecursionlimit(100001)
n=int(input())
nums=list(map(int,input().split(" ")))
res=0
M=max(nums)
Mi=min(nums)
m=M-Mi+1
cnt_num=[0]*(m)
for i in nums:
    cnt_num[i-Mi]+=1
memo=[-1]*(m)
def rec(i):
    if i>=m:
        return 0
    if cnt_num[i]==0:
        memo[i]=rec(i+1)
    if memo[i]==-1:
        memo[i]=max(cnt_num[i]*(i+Mi)+rec(i+2),rec(i+1))
    return memo[i]
print(rec(0)) 