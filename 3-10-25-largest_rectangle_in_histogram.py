class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l=len(heights)
        prev_smaller=[-1]*l
        next_smaller=[l]*l
        stck=[]
        for i in range(l):
            while(len(stck)!=0 and heights[i]<=stck[-1][0]):
                stck.pop()
            if stck!=[]:
                prev_smaller[i]=stck[-1][1]
            stck.append((heights[i],i))
        stck=[]
        for i in range(l-1,-1,-1):
            while(len(stck)!=0 and heights[i]<=stck[-1][0]):
                stck.pop()
            if stck!=[]:
                next_smaller[i]=stck[-1][1]
            stck.append((heights[i],i))
        res=[]
        for i in range(l):
            res.append(heights[i]*(next_smaller[i]-(prev_smaller[i]+1)))
        return max(res)