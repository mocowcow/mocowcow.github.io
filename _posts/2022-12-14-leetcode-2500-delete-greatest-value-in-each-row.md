--- 
layout      : single
title       : LeetCode 2500. Delete Greatest Value in Each Row
tags        : LeetCode Easy Array Medium
---
周賽323。這幾天鳥事情比較多，拖到現在才寫題解。  
這題作為Q1有點麻煩，雖然一樣可以暴力解，但是非常繁瑣。  

# 題目
輸入大小為m*n且只含正整數的grid。  

執行以下動作直到grid為空：  
- 刪除每一列中最大的元素。若有多個相等的最大元素，擇一刪除  
- 將被刪除元素最大值加入答案中  

# 解法
要先把每一列中最大的刪掉，然後找到刪掉中最大的。  
可以先把各列排序(遞增遞減無所謂)，這樣同一行中都會是該列中第i大的元素。  

時間瓶頸在於各列的排序，為O(N log N\*M)。空間為O(1)。  

```python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        ans=0

        for r in grid:r.sort()    
        
        for c in range(N):
            mx=0
            for r in grid:
                mx=max(mx,r[c])
            ans+=mx
        
        return ans
```

另外提供比較神奇的python做法。  
一樣先排序，利用zip函數將將矩陣拆包，讓同一行的函數被放在一起，直接使用max函數就可以找到每次刪除中的最大值。  

```python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for r in grid:r.sort()
        return sum(max(c) for c in zip(*grid))
```