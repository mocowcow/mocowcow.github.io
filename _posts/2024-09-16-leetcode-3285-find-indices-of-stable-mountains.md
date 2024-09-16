---
layout      : single
title       : LeetCode 3285. Find Indices of Stable Mountains
tags        : LeetCode Easy Simulation
---
biweekly contest 139。  

## 題目

有 n 座山排成一列，每座山高度不同。  
輸入整數陣列 height，其中 height[i] 代表第 i 座山的高度。還有一個整數 threshold。  

若某座山 i 存在**左側相鄰**、且高度**嚴格大於** threshold 的山，則稱為**穩定的**。  
注意：第 0 座山不可能是穩定的。  

回傳包含所有**穩定的山**的索引，可以是任意順序。  

## 解法

模擬題，照做就是了。  

時間複雜度 O(N)。  
空間複雜度 O(1)，答案空間不計入。  

```python
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        N = len(height)
        ans = []
        for i in range(1, N):
            if height[i - 1] > threshold:
                ans.append(i)

        return ans
```

歡樂一行版本。  

```python
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i-1] > threshold]
```
