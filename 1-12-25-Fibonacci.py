class Solution:
    def fib(self, n: int) -> int:
        if n>0:
            memo=[1 for x in range(n)]
            def fibo(n):
                if n<3:
                    return 1
                if memo[n-2]==1:
                    memo[n-2]=fibo(n-1)
                if memo[n-3]==1:
                    memo[n-3]=fibo(n-2)
                memo[n-1]=memo[n-2]+memo[n-3]
                return memo[n-1]
            return fibo(n)
        return 0
