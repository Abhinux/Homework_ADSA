class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            if i not in res:
                if i in nums2:
                    res.append(i)
        return res

        
        # a=set(nums1)
        # b=set(nums2)
        # return a&b