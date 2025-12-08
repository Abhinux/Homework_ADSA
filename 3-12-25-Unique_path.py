class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[-1 for I in range(n)] for j in range(m)]
        def rec(x, y) :
            if x==m-1 or y==n-1:
                return 1
            if memo[x][y]==-1:
                memo[x][y]=rec(x+1, y)+rec(x, y+1)
            return memo[x][y]
        return rec(0, 0)