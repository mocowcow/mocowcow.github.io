--- 
layout      : single
title       : LeetCode 2679. Sum in a Matrix
tags        : LeetCode Medium Array Matrix Sorting
---
雙周賽104。

# 題目
輸入二維整數陣列nums，代表一個矩陣。你的初始分數為0。  
執行以下動作直到矩陣為空：  
- 從每一列中選取一個最大的數字，並將其刪除  
- 在本次被刪除的數字中，將最大的數字加入**分數**  

回傳最後的**分數**。  

# 解法
先把每一列都排序，這樣只要同一行中的最大值就是分數，將分數加到答案。  

瓶頸在於排序，時間複雜度O(MN log N)，其中M為列數，N為行數。  
空間複雜度O(1)。  

```python
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        M,N=len(nums),len(nums[0])
        ans=0
        
        for row in nums:
            row.sort()
            
        for c in range(N):
            mx=0
            for r in range(M):
                mx=max(mx,nums[r][c])
            ans+=mx
            
        return ans
```

也可以利用zip函數將排序好的每個列都綁成一個list，直接max就可以取最大值。  

```python
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
            
        return sum(max(col) for col in zip(*nums))
```