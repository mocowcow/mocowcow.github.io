---
layout      : single
title       : LeetCode 1584. Min Cost to Connect All Points
tags 		: LeetCode Medium Array Graph Heap MST 
---
每日題。leetcode站上似乎沒多少和最小生成樹相關的題目。

# 題目
輸入二維陣列pointers，代表各點points[i]的(x,y)座標。  
求將所有點連接的最小**曼哈頓距離**成本為多少。  
(x1,y1)和(x2,y2)兩點的**曼哈頓距離**為abs(x1-x2)+abs(y1-y2)。

# 解法
將N個點連接，需要N-1個邊。
一開始寫了三個迴圈的暴力法版本：重複N-1次，每次在所有點中找到最短的連線，複雜度O(N^3)，不意外的拿到TLE。  

既然要找最短的連線，使用heap可以節省不少時間。  
長度N的陣列conn代表第i個點是否已經被連線到，整數used紀錄已經連線的點有多少。  
每次都以points[0]為起點，將0和所有其他點的距離加入heap中。  
重複以下連線動作，直到所有點都連線完成為止：  
1. 取出heap中最短的邊，如果候選點cand已經有連線了，那就略過，找下一條邊  
2. 將cand標記為已連線，連線點used+1，將邊的成本加入ans中  
3. 以cand為出發點，對所有還沒有連線的點j，把cand到j的邊加入heap中  

回傳ans就是最小成本。  

寫完看討論區才知道，原來這好像就是Prim's Algorithm。  
因為要建立N^2個邊，複雜度是O(N^2)，加上找N次最短邊成本應該是N*(log N^2)，整體複雜度還是(N^2)。

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dis(i, j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])

        N = len(points)
        h = []
        conn = [False]*N
        conn[0] = True
        used = 1
        ans = 0
        # init routes from points[0]
        for j in range(1, N):
            heappush(h, (dis(0, j), j))
        while used < N:
            d, cand = heappop(h)
            if conn[cand]:
                continue
            conn[cand] = True
            # print('conncet', points[adj])
            used += 1
            ans += d
            # add routes from adj
            for j in range(1, N):
                if conn[j] == False:
                    heappush(h, (dis(cand, j), j))

        return ans
```

官方的解法，使用cost陣列表示連接i點的最小成本，每次連接完新的點後更新最小值。  
複雜度一樣O(N^2)，執行起來比上面方法慢一些。

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dis(i, j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])

        N = len(points)
        conn = [False]*N
        cost = [math.inf]*N
        cost[0]=0
        ans=0
        for _ in range(N):
            cand=None
            mn=math.inf
            for i in range(N):
                if conn[i]==False and cost[i]<mn:
                    mn=cost[i]
                    cand=i
            # conncect
            conn[cand]=True
            ans+=mn
            # update min costs
            for j in range(N):
                if conn[j]==False:
                    cost[j]=min(cost[j],dis(cand,j))
   
        return ans
```