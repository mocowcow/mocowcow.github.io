---
layout      : single
title       : LeetCode 2951. Find the Peaks
tags        : LeetCode Easy Array Simulation
---
周賽374。放水題，好康的還在後頭。

## 題目

輸入陣列mountain。你的目標是找到mountain中的所有**山峰**。  
以**任意順序**回傳所有**山峰**索引。  

注意：  

- **山峰**指的是某個元素**嚴格**大於其左右元素  
- 第一個元素和最後一個元素**不是**山峰  

## 解法

按照題意模擬。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        N=len(mountain)
        ans=[]
        for i in range(1,N-1):
            if mountain[i-1]<mountain[i] and mountain[i]>mountain[i+1]:
                ans.append(i)
                
        return ans  
```
