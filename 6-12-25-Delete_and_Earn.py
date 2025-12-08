class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m=min(nums)
        M=max(nums)
        Len_cnt=M-m+1
        cnt=[0]*Len_cnt
        for i in nums:
            cnt[i-m]+=1
        memo=[-1]*Len_cnt
        def rec(i):
            if i>=Len_cnt:
                return 0
            if cnt[i]==0:
                memo[i]=rec(i+1)
            if memo[i]==-1:
                memo[i]=max(cnt[i]*(i+m)+rec(i+2),rec(i+1))
            return memo[i]
        return rec(0)