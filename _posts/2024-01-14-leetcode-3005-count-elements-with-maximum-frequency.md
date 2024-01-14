---
layout      : single
title       : LeetCode 3005. Count Elements With Maximum Frequency
tags        : LeetCode Easy Array
---
周賽380。

## 題目

輸入正整數陣列 nums。  

求 nums 中有多少個元素，其出現頻率等於**最大**的元素**出現頻率**。  

## 解法

要看清楚，是問有**幾個**元素的頻率等於最大頻率，不是有**幾種**。  

先遍歷 nums 統計元素頻率。  
在遍歷頻率遍歷找到最大頻率 mx。  
最後遍歷 nums 看有有哪些元素的頻率等於 mx。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = Counter(nums)
        mx = max(d.values())
        
        return sum(d[x] == mx for x in nums)
        # return sum(v for v in d.values() if v == mx)
```
