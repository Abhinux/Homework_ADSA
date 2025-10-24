class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if target>nums[r]:
            return r+1
        if target<nums[l]:
            return 0
        while(l<r):
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                r=mid
            else:
                l=mid+1
        return l