---
layout      : single
title       : LeetCode 2965. Find Missing and Repeated Values
tags        : LeetCode Easy Array Matrix HashTable Simulation
---
周賽376。

## 題目

有個n\*n的二維矩陣matrix，由[1, n^2]之間的元素所組成。  
每個元素正好出現一次，除了其中一個元素a出現兩次，還有元素b沒有出現。  

回傳長度為2的陣列ans，其中ans[0]和ans[1]分別代表a, b的值。  

## 解法

直接統計1\~n^2所有元素的出現次數，再遍歷一次就能找到a, b。  

時間複雜度O(n^2)。  
空間複雜度O(n^2)。  

```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N=len(grid)
        d=Counter(x for row in grid for x in row)
        
        ans=[None]*2
        for i in range(1,N**2+1):
            if d[i]==2:
                ans[0]=i
            elif d[i]==0:
                ans[1]=i
                
        return ans
```
