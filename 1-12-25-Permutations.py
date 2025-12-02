class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def gen(s,nums,i):
            if i==0:
                res.append(s)
                return
            for j in range(i):
                gen(s+[nums[j]],nums[:j]+nums[j+1:],i-1)
        gen([],nums,n)
        return res