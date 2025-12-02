class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def return_sub(i,res1):
            if i<n:
                return_sub(i+1,res1+[nums[i]])
                return_sub(i+1,res1)
            else:
                res.append(res1)
        return_sub(0,[])
        return res