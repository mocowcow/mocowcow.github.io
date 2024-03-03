---
layout      : single
title       : LeetCode 3065. Minimum Operations to Exceed Threshold Value I
tags        : LeetCode Easy Array
---
雙周賽125。

## 題目

輸入整數陣列 nums，以及整數 k。  

每次操作，你可以從 nums 中移除一個最小的元素。  

求**最少**需要幾次操作，才能使得 nums 中所有元素都**大於等於** k。  

## 解法

刪除順序不重要。有幾個元素小於 k，就要刪幾次。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for x in nums:
            if x < k:
                ans += 1
        return ans
        # return sum(x < k for x in nums)
```
