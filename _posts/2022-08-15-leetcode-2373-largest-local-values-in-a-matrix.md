--- 
layout      : single
title       : LeetCode 2373. Largest Local Values in a Matrix
tags        : LeetCode Easy Array Matrix 
---
周賽306。乍看很麻煩，其實只要四個迴圈，考察簡單的分析能力。  

# 題目
輸入N*N的整數矩陣grid。  
生成一個大小為(N-2)*(N-2)的整數矩陣maxLocal，滿足：  
- maxLocal[i][j]為以第i+1行和j+1列為中心，3*3範圍內的最大值   

換句話說，要在網格中的每個連續3*3矩陣中找到最大值。  
回傳生成的矩陣。  

# 解法
有一個小技巧：與其列舉每個3*3子矩陣的中心點，不如改為列舉左上角，這樣求範圍內數值會方便很多。  

題目很好心的說了答案的邊長為M=N-2，那麼會有M*M個子矩陣。  
列舉所有子矩陣的左上角(r,c)，再遍歷該點所產生3*3子矩陣的所有元素，找到最大值。  

```python
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N=len(grid)
        M=N-2
        ans=[[0]*M for _ in range(M)]
        
        for r in range(M):
            for c in range(M):
                for rr in range(r,r+3):
                    for cc in range(c,c+3):
                        ans[r][c]=max(ans[r][c],grid[rr][cc])
        
        return ans
```
