class Solution:
    def reverseFirstK(self, q, k):
        #code here 
        if len(q)>=k:
            l=[]
            r=[]
            for i in range(k):
                l.append(q.popleft())
            while(q):
                r.append(q.popleft())
            L=len(l)
            for i in range(L//2):
                l[i],l[L-i-1]=l[L-i-1],l[i]
            res=deque()
            for i in l:
                res.append(i)
            for i in r:
                res.append(i)
            return res
        else:
            return q