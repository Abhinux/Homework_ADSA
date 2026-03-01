1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        n=len(grid)
4        pq=[]
5        heapq.heapify(pq)
6        heapq.heappush(pq,(grid[0][0],0,0))
7        res=[[float('inf') for _ in range(n)] for x in range(n)]
8        res[0][0]=grid[0][0]
9        dx=[0,0,1,-1]
10        dy=[1,-1,0,0]
11        while(pq):
12            cost,r,c=heapq.heappop(pq)
13            for i in range(4):
14                nr=r+dx[i]
15                nc=c+dy[i]
16                if 0<=nr<n and 0<=nc<n:
17                    cur_cost=max(cost,grid[nr][nc])
18                    if cur_cost<res[nr][nc]:
19                        res[nr][nc]=cur_cost
20                        heapq.heappush(pq,(cur_cost,nr,nc))
21
22        a=res[n-1][n-1]
23        if a==float('inf'):
24            return -1
25        else:
26            return a