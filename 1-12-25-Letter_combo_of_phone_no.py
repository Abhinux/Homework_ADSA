class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=[]
        n=len(digits)
        # for i in digits:
        #     if res==[]:
        #         res=dig[i]
        #     else:
        #         n=len(res)
        #         cnt=0
        #         while(cnt<n):
        #             a=res[0]
        #             for j in dig[i]:
        #                 res.append(a+j)
        #             res.pop(0)
        #             cnt+=1
        def gen(digits,i,s):
            if i==n:
                res.append(s)
                return
            for j in dig[digits[i]]:
                gen(digits,i+1,s+j)
        gen(digits,0,"")
        return res

