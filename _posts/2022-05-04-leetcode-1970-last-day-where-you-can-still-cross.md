--- 
layout      : single
title       : LeetCode 1970. Last Day Where You Can Still Cross
tags        : LeetCode Hard Array Matrix BinarySearch BFS UnionFind
---
相似題[2258. escape the spreading fire]({% post_url 2022-05-01-leetcode-2258-escape-the-spreading-fire %})，但這題還可以用併查集來解。

# 題目
輸入整數row, col代表一個索引從1開始的row*col矩陣，從一開始每格都是陸地。  
另外輸入二維陣列cells，cells[i]=(r,c)代表在第i天過後，第(r,c)的格子會被水淹沒。  
你可以朝上下左右四個方向移動，從第一列出發，試著抵達最後一列，且只能經過陸地格子。  
求能夠成功從最上面走到最下面的**最後一天**。

# 解法
畢竟這題和逃離火場有點像，就先試著用bfs+二分搜來寫。  

處理二分搜的邏輯，第0天沒有任何水，一定可以通過，下界定為0。上界隨便定為總天數，也就是最後一天。其實理論上能通過的最後一天是總天數-列數-1，但無所謂。  
如果第mid天能成功通行，則mid天以前也都能過，更新下界為mid；mid不通則更新上界為mid-1。考慮lo=0, hi=1的狀況，若取左中位數mid=0，更新下界會死循環，故改取右中位數。  

再來是bfs的部分，一開始先預處理頂端的所有出發點，避免每次bfs重複計算。  
根據天數決定要加入哪幾格水域，其實也不用真的去生成m*n的矩陣，直接把水域和走過的位置通通裝在visited集合裡面就好。  
開始bfs，若當前位置不合法則跳過；抵達底端回傳true，否則向四位置擴散。能走的格子全部走完代表無法抵達，回傳false。
  
```python
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        M,N=row,col
        start=[(0,c) for c in range(N)] # start from top
        
        def canCross(day):
            visited=set()
            for i in range(day): # flood
                r,c=cells[i]
                visited.add((r-1,c-1))
            q=deque(start) 
            while q:
                r,c=q.popleft()
                if not (0<=r<M and 0<=c<N) or (r,c) in visited:
                    continue
                if r==M-1: # reach bottom
                    return True
                visited.add((r,c))
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    q.append((nr,nc))
            return False
        
        lo=0
        hi=len(cells)
        while lo<hi:
            mid=(lo+hi+1)//2
            if not canCross(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
```


UF

```python
code here
```

