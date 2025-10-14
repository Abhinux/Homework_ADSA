#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        res=[]
        for i in pre_exp[::-1]:
            if i=="*"or i=="-"or i=="+"or i=="/"or i=="^":
                a=res.pop()
                b=res.pop()
                res.append(a+b+i)
            else:
                res.append(i)
        return res[0]
            