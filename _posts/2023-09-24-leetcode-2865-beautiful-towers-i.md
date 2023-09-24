---
layout      : single
title       : LeetCode 2865. Beautiful Towers I
tags        : LeetCode Medium Array Simulation
---
周賽364。

## 題目

輸入長度n的整數陣列maxHeights。  

你要建造n個塔，第i個塔在座標i上，且高度為heights[i]。  

一個**美麗的**塔，配置方式需要符合以下條件：  

- 1 <= heights[i] <= maxHeights[i]  
- heights是山形陣列  

山形陣列heights必須存在一個索引i：  

- 對於所有 0 < j <= i ，所有 heights[j - 1] <= heights[j]  
- 對於所有 i <= k < n - 1 ，所有 heights[k + 1] <= heights[k]  

求**美麗塔**的**最大高度總和**。  

## 解法

簡單講就是要選一個山頂i，以i為中心，往左右要呈單調遞減。例如：[1,2,3,3,1]。  
但是每個索引j同時要受到maxHeights[j]的限制。  

測資不大可以暴力模擬，枚舉索引i作為山頂，往左右擴散處理。  
得出以i為山頂的各塔高度tower後，以tower總和更新答案。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        N=len(maxHeights)
        ans=0
        
        for i in range(N):
            tower=[0]*N
            tower[i]=maxHeights[i]
            
            for j in range(i+1,N):
                tower[j]=min(tower[j-1],maxHeights[j])
                
            for j in reversed(range(i)):
                tower[j]=min(tower[j+1],maxHeights[j])
                
            ans=max(ans,sum(tower))
            
        return ans
```
