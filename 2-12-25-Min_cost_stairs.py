class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        memo=[-1 for x in range(n)]
        def rec(i):
            if i>=n:
                return 0
            if memo[i]==-1:
                memo[i]=cost[i]+min(rec(i+1),rec(i+2))
            return memo[i]
        return min(rec(0),rec(1))