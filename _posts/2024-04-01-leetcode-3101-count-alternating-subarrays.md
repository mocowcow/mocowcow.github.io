---
layout      : single
title       : LeetCode 3101. Count Alternating Subarrays
tags        : LeetCode Medium Array Math TwoPointers
---
周賽 391。又是分組循環的一天。  

## 題目

輸入二進位陣列 nums。  

如果一個陣列中不存在**相鄰且相同**的元素，則稱為**交替的**。  

求 nums 中有多少**交替的**子陣列。  

## 解法

一個長度為 size 的交替陣列，其產生的所有子陣列**必定也是交替的**。  
共可以產生 size \* (size + 1) / 2 個子陣列。  

所以我們只需要在 nums 中將交替的元素**分組**，分割成數個盡可能長的**交替**陣列。  
然後對每組分別計算子陣列數量即可。  
例如："101101" 可以變成 "101" 和 "101"，答案是 6 + 6 = 12。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        i = 0
        while i < N:
            # nums[i..j] is alternating
            j = i
            while j + 1 < N and nums[j] != nums[j + 1]:
                j += 1
                
            size = j - i + 1
            ans += size * (size + 1) // 2
            i = j + 1
            
        return ans
```
