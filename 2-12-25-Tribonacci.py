class Solution:
    def tribonacci(self, n: int) -> int:
        memo=[0]*n
        def tribo(n):
            if n==0:
                return 0
            if n<3:
                return 1
            if memo[n-1]==0:
                memo[n-1]=tribo(n-1)+tribo(n-2)+tribo(n-3)
            return memo[n-1]
        return tribo(n)