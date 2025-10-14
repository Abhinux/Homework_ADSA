#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        res=[]
        for i in postfix:
            if i=="+"or i=="-"or i=="*"or i=="/"or i=="^":
                b=res.pop()
                a=res.pop()
                res.append("("+a+i+b+")")
            else:
                res.append(i)
        return res[0]