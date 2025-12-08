class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        memo=[[101 for i in range(n)] for j in range(m)]
        def rec(x,y):
            if y==n or y<0:
                return 100000000
            if x==m:
                return 0
            if memo[x][y]==101:
                memo[x][y]=matrix[x][y]+min(rec(x+1,y),rec(x+1,y-1),rec(x+1,y+1))
            return memo[x][y]
        res=float("inf")
        for i in range(n):
            res=min(rec(0,i),res)
        return res
