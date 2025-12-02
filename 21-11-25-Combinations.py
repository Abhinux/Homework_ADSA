class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        def return_sub(i,res1):
            if sum(res1)<target and i<n:
                return_sub(i,res1+[candidates[i]])
                return_sub(i+1,res1)
            else:
                if sum(res1)==target:
                    res.append(res1)
        return_sub(0,[])
        return res
        