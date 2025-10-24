class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while(l<r):
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        k=l
        l=0
        r=n-1
        while(l<=r):
            mid=(l+r)//2
            rot_mid=(mid+k)%n
            if nums[rot_mid]==target:
                return rot_mid
            if nums[rot_mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1