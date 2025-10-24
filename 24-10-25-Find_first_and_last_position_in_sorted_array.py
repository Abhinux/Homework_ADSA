class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        cnt=nums.count(target)
        if nums:
            if nums[l]==target:
                return (0,cnt-1)
            elif nums[r]==target:
                return (r-cnt+1,r)
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==target:
                    while(mid>0):
                        if nums[mid-1]==target:
                            mid-=1
                        else:
                            break
                    return (mid,mid+cnt-1)
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        return (-1,-1)