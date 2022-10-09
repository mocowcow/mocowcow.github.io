--- 
layout      : single
title       : LeetCode 2428. Maximum Sum of an Hourglass
tags        : LeetCode Medium Array Matrix
---
周賽313。

# 題目
輸入一個m\*n的整數矩陣grid。  
**沙漏**指的是矩陣中的某一部分，如下圖：  
![沙漏圖片](https://assets.leetcode.com/uploads/2022/08/21/img.jpg)  

求所有沙漏的最大總和。  
注意，沙漏不可旋轉，且必須完整出現在矩陣中。  

# 解法
沙漏本身只佔了7個格子，也就是7次運算。而矩陣最大是150\*150，暴力窮舉所有沙漏也只要150\*150\*7=157500次運算，還在合理範圍內。  
順帶一提，如果沙漏的格子很長，可能就要考慮用2D前綴和來降低複雜度。  

根據窮舉的方法不同，這題難度可能會有一些差異。窮舉沙漏中心點，xy軸和中心點距離最多1，只需要適時+1或-1；如果窮舉沙漏左上角，就會要多打很多加號，而且會出現+1、+2的情況。  

時間複雜度O(M\*N*)，空間複雜度O(1)。  

```python
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        ans=0
        
        for r in range(1,M-1):
            for c in range(1,N-1):
                val=grid[r][c]
                val+=grid[r+1][c-1]+grid[r+1][c]+grid[r+1][c+1]
                val+=grid[r-1][c-1]+grid[r-1][c]+grid[r-1][c+1]
                ans=max(ans,val)
        
        return ans
```
