class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        memo=[[-1 for i in range(n)] for j in range(m)]
        if obstacleGrid[m-1][n-1]==0:
            def rec(x,y):
                if (x>m-1 or y>n-1):
                    return 0
                if x==m-1 and y==n-1:
                    return 1
                if obstacleGrid[x][y]==1:
                    return 0
                if memo[x][y]==-1:
                    memo[x][y]=rec(x+1,y)+rec(x,y+1)
                return memo[x][y]
            return rec(0,0)
        return 0