--- 
layout      : single
title       : LeetCode 2662. Minimum Cost of a Path With Special Roads
tags        : LeetCode Medium Array Graph BFS Heap HashTable
---
周賽343。腦子差點卡死，這題有點繞彎，而且一堆xy有夠麻煩，應該算偏難的Q3。  

# 題目
輸入陣列start = [startX, startY]，代表你將從(startX, startY)出發。  
還有陣列target = [targetX, targetY]，代表目的地(targetX, targetY)。  

從(x1, y1)移動到(x2, y2)的成本為|x2 - x1| + |y2 - y1|。  

有一些特殊的道路，由二維陣列specialRoads表示，其中specialRoads[i] = [x1i, y1i, x2i, y2i, costi]代表從(x1i, y1i) 到 (x2i, y2i)的成本為costi。  
你可以使用各特殊道路任意次。  

求從(startX, startY)到(targetX, targetY)的**最低成本**。  

# 解法
普通移動的成本就是**曼哈頓距離**。  

從起點出發時，你有兩種選擇：  
- 直接走到終點  
- 先走到某個點，過特殊道路，再到終點  

如果後者比前者成本還低，那就代表走這條特殊道路是更佳的。那再繼續判斷有沒有別條路可以繼續省？  
發現根本就是dijkstra最短路：優先選成本最低的路徑，第一個到達終點的就是最佳解。  

把每個特殊路徑終點的視為節點，共有V個，而可移動的邊共有E=V^2個。  

時間複雜度O(E + V log V)。  
空間複雜度O(E + V)。  

```python
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        
        def dist(x1,y1,x2,y2):
            return abs(x1-x2)+abs(y1-y2)
        
        x,y=start
        end_x,end_y=target
        
        vis=set()
        h=[]
        heappush(h,[0,x,y])
        
        while h:    
            cost,x,y=heappop(h)
            
            if x==end_x and y==end_y:
                return cost
            
            if (x,y) in vis:
                continue
            vis.add((x,y))
            
            # simple move
            new_cost=cost+dist(x,y,end_x,end_y)
            heappush(h,[new_cost,end_x,end_y])
            
            # use special
            for x1,y1,x2,y2,c in specialRoads:
                new_cost=cost+dist(x,y,x1,y1)+c
                heappush(h,[new_cost,x2,y2])
```
