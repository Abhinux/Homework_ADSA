class Solution:
    def trap(self, height: List[int]) -> int:
        Length=len(height)
        max=height[0]
        max_idx=0
        water=0
        n=len(height)
        for i in range(1,n):
            if height[i]>max:
                max=height[i]
                max_idx=i
        prev=0
        for i in range(max_idx):
            if height[i]>prev:
                prev=height[i]
            else:
                water+=(prev-height[i])
        prev=0
        for j in range(Length-1,max_idx,-1):
            if height[j]>prev:
                prev=height[j]
            else:
                water+=(prev-height[j])
        return water

