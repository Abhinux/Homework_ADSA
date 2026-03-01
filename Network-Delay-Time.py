1import heapq
2class Solution:
3    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
4        res=[float('inf') for _ in range(n)]
5        res[k-1]=0
6        for i in range(n-1):
7            for u,v,c in times:
8                u-=1
9                v-=1
10                if res[u]!=float('inf'):
11                    res[v]=min(res[v],res[u]+c)
12        a=max(res)
13        if a==float('inf'):
14            return -1
15        else:
16            return a
17