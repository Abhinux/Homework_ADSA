class Solution:
    def validStrings(self, n: int) -> List[str]:
        # res=["0","1"]
        # i=1
        # while(i<n):
        #     m=len(res)
        #     while(m>0):
        #         a=res.pop(0)
        #         if a[-1]=="0":
        #             res.append(a+"1")
        #         else:
        #             res.append(a+"0")
        #             res.append(a+"1")
        #         m-=1
        #     i+=1
        res=[]
        def gen(s,n):
            if n==0:
                res.append(s)
                return
            if s[-1]=="0":
                gen(s+"1",n-1)
            else:
                gen(s+"0",n-1)
                gen(s+"1",n-1)
        gen("0",n-1)
        gen("1",n-1)
        return res


