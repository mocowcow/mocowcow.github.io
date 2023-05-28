--- 
layout      : single
title       : LeetCode 2711. Difference of Number of Distinct Values on Diagonals
tags        : LeetCode Medium Array Matrix HashTable Simulation
---
周賽347。沒什麼難度，但就是很囉唆的題。  

# 題目
輸入m\*n的二維整數陣列grid，你必須找到同為m\*n的矩陣answer。  

answer中每個格子(r,c)的值如下計算：  
- topLeft[r][c]是(r,c)左上對角線中，**不同**值的數量  
- bottomRight[r][c]是(r,c)右下對角線中，**不同**值的數量  
- answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|  

回傳矩陣answer。  

# 解法
按照題意模擬，將左上右下對角線的元素去重後計算絕對差。  
左上就把行列都減1，右下都加1。  

對角線長度為min(M,N)，時間複雜度O(MN \* min(M,N))。  
忽略輸出答案矩陣，空間複雜度O(min(M,N))。  

```python
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        M,N=len(grid),len(grid[0])
        ans=[[0]*N for _ in range(M)]
        
        for r in range(M):
            for c in range(N):
                # lt
                lt=set()
                rr,cc=r-1,c-1
                while rr>=0 and cc>=0:
                    lt.add(grid[rr][cc])
                    rr-=1
                    cc-=1
                    
                # rb
                rb=set()
                rr,cc=r+1,c+1
                while rr<M and cc<N:
                    rb.add(grid[rr][cc])
                    rr+=1
                    cc+=1
                
                ans[r][c]=abs(len(lt)-len(rb))
        
        return ans
```
