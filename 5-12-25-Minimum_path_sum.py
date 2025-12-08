class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        memo=[[-1 for i in range(n)] for j in range(m)]
        def rec(x,y):
            if x==m or y==n:
                return 200000
            if x==m-1 and y==n-1:
                memo[x][y]=grid[x][y]
            if memo[x][y]==-1:
                memo[x][y]=grid[x][y]+min(rec(x+1,y),rec(x,y+1))
            return memo[x][y]
        rec(0,0)
        return memo[0][0]