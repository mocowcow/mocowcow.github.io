--- 
layout      : single
title       : LeetCode 2639. Find the Width of Columns of a Grid
tags        : LeetCode
---
雙周賽102。初始值設錯吃到一個WA，我自己都覺得很瞎。  

# 題目
輸入M\*N的矩陣grid。  
欄位的寬度為該行整數中**最長的字串長度**。  

- 例如：grid = [[-10], [3], [12]]，最長的整數為-10，則該行寬度為3  

回傳大小為n的整數陣列ans，其中ans[i]代表第i行的寬度。  

整數x是len位數，若x為非負數則長度為len；若為負數則為len+1。  

# 解法
特別注意，題目要求是**各行**的最大長度，也就是直的往下看。  

直接把整數轉成字串後判斷長度最方便，不用考慮正負或是零。  

時間複雜度O(MN log (MX))，其中M為列數，N為行數，MX為max(nums[r][c])-min(nums[r][c])。忽略輸出答案陣列，空間複雜度O(1)。  

```python
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        M,N=len(grid),len(grid[0])
        row=0
        ans=[]
        
        for c in range(N):
            mx=0
            for r in range(M):
                x=str(grid[r][c])
                mx=max(mx,len(x))
            ans.append(mx)
            
        return ans
```
