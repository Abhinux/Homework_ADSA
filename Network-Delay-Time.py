1import heapq
2class Solution:
3    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
4        res=[float('inf') for _ in range(n)]
5        adj=[list() for _ in range(n)]
6        for u,v,c in times:
7            adj[u-1].append((v-1,c))
8        pq=[]
9        heapq.heapify(pq)
10        heapq.heappush(pq,(0,k-1))
11        res[k-1]=0
12        while(pq):
13            c,u=heapq.heappop(pq)
14            if c>res[u]:
15                continue
16            for v,new_cost in adj[u]:
17                cur_cost=new_cost+c
18                if cur_cost<res[v]:
19                    res[v]=cur_cost
20                    heapq.heappush(pq,(cur_cost,v))
21
22        act_res=max(res)
23        if act_res==float('inf'):
24            return -1
25        else:
26            return act_res
27
28