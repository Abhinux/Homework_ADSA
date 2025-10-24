class Solution:
    def generateBinary(self, n):
        res = []
        a="1"
        b="0"
        q = deque()
        q.append(a)
        while n > 0:
            s1 = q.popleft()
            res.append(s1)
            if len(q) < n:
                q.append(s1 + b)
                q.append(s1 + a)
            n-=1
        return res
            
        