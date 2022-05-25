--- 
layout      : single
title       : LeetCode 1605. Find Valid Matrix Given Row and Column Sums
tags        : LeetCode Medium Array Matrix Greedy
---
模擬雙周賽36。很神奇的一題，老實說沒什麼特別想法，就試著亂塞，結果就過了。

# 題目
輸入兩個非負整數陣列rowSum和colSum，其中rowSum[i]是第i列中元素的總和，而colSum[j]是第j行元素的總和。  
回傳任一滿足rowSum和colSum要求的非負整數矩陣。答案保證至少有一個。

# 解法
因為不會出現負數，所以規則就單純很多，在某個位置使用某數，只會讓總體的需求減少，而不會增加。  
那麼就盡可能的使用較大的數，趕快滿足總和要求，剩下的格子全部維持0就好。  

例如rowSum=[10,5], colSum=[10,5]  
> r=0, c=0 塞入10  
> ans=[[10,0],[0,0]]  rowSum=[0,5], colSum=[0,5]  
> r=1, c=0 塞入0  
> r=0, c=1 塞入0  
> r=1, c=1 塞入5  
> ans=[[10,0],[0,5]]  rowSum=[0,0], colSum=[0,0]  

```python
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        M=len(rowSum)
        N=len(colSum)
        ans=[[0]*N for _ in range(M)]
        
        for r in range(M):
            for c in range(N):
                x=min(rowSum[r],colSum[c])
                ans[r][c]=x
                rowSum[r]-=x
                colSum[c]-=x
                
        return ans
```
