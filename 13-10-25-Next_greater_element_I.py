class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res2=[-1]*len(nums2)
        stck=[nums2[-1]]
        for i in range(len(nums2)-2,-1,-1):
            while(stck and stck[-1]<=nums2[i]):
                stck.pop()
            if stck:
                res2[i]=stck[-1]
            stck.append(nums2[i])
        res=[]
        for j in nums1:
            ind=nums2.index(j)
            res.append(res2[ind])
        return res
