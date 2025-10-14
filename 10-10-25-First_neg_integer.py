
class Solution:
    def firstNegInt(self, arr, k): 
        n=len(arr)
        res=[0]*(n-k+1)
        q=[]
        for i in range(k):
            if arr[i]<0:
                q.append(i)
        if q:
            res[0]=arr[q[0]]
        p=0
        for i in range(k,n):
            if q and q[0]==p:
                q.pop(0)
            if arr[i]<0:
                q.append(i)
            if q:
                res[p+1]=arr[q[0]]
            p+=1
        
        return res