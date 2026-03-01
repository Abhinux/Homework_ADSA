1class Solution:
2    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
3        n=len(passingFees)
4        adj=[{} for _ in range(n)]
5        for u,v,c in edges:
6            try:
7                adj[u][v]=min(adj[u][v],c)
8                adj[v][u]=min(adj[v][u],c)
9            except:
10                adj[u][v]=c
11                adj[v][u]=c
12        pq=[]
13        heapq.heapify(pq)
14        heapq.heappush(pq,(passingFees[0],0,0))
15        res=[[float('inf') for _ in range(maxTime+1)] for x in range(n)]
16        res[0][0]=passingFees[0]
17        while(pq):
18            cost,u,time=heapq.heappop(pq)
19            if u==n-1:
20                return cost
21            for v in adj[u]:
22                cur_fees=cost+passingFees[v]
23                cur_time=time+adj[u][v]
24                if cur_time>maxTime or res[v][cur_time]<cur_fees:
25                    continue
26                if cur_fees<res[v][cur_time]:
27                    res[v][cur_time]=cur_fees
28                    heapq.heappush(pq,(cur_fees,v,cur_time))
29        return -1