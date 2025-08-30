class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=0
        res=1
        n=len(s)
        if s!="":
            curr_res=0
            for i in range(1,n):
                same=False
                for j in range(x,i):
                    if s[j]==s[i]:
                        x=j+1
                        same=True
                        break
                curr_res=i-x+1
                if same==False and curr_res>res:
                    res=curr_res
        else:
            res=0
        return res
