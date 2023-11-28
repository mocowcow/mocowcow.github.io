---
layout      : single
title       : LeetCode 2946. Matrix Similarity After Cyclic Shifts
tags        : LeetCode Easy Array Matrix Simulation
---
周賽373。

## 題目

輸入m\*n，且索引從0開始的矩陣mat，還有一個整數k。  
你必須將mat中**奇數**列循環**右移**k次，而**偶數**列循環**左移**k次。  

若位移後的矩陣與初始矩陣相同則回傳true，否則回傳false。  

## 解法

測資不大，直接照著描述做。  
雙向隊列deque很適合模擬這種左右移的操作。  

時間複雜度O(mnk)。  
空間複雜度O(n)。  

```python
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i,row in enumerate(mat):
            q=deque(row)
            if i%2==0: # odd right
                for _ in range(k):
                    t=q.pop()
                    q.appendleft(t)
            else: # even left
                for _ in range(k):
                    t=q.popleft()
                    q.append(t)
            #check
            for x,y in zip(q,row):
                if x!=y:
                    return False
                
        return True
```
