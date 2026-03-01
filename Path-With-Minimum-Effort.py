1class Solution:
2    def minimumEffortPath(self, heights: List[List[int]]) -> int:
3        n=len(heights)
4        m=len(heights[0])
5        dx=[0,0,1,-1]
6        dy=[1,-1,0,0]
7        def valid(x,y):
8            return x>-1 and x<n and y>-1 and y<m
9        pq=[]
10        heapq.heapify(pq)
11        heapq.heappush(pq,(0,(0,0)))
12        res=[[float('inf') for _ in range(m)] for x in range(n)]
13        res[0][0]=0
14        while(pq):
15            cur=heapq.heappop(pq)
16            cos=cur[0]
17            coord=cur[1]
18            if cos>res[coord[0]][coord[1]]:
19                continue
20            for i in range(4):
21                r=coord[0]+dx[i]
22                c=coord[1]+dy[i]
23                if valid(r,c):
24                    new=max(cos,abs(heights[coord[0]][coord[1]]-heights[r][c]))
25                    if res[r][c]>new:
26                        res[r][c]=new
27                        heapq.heappush(pq,(new,(r,c)))
28        return res[n-1][m-1]
29