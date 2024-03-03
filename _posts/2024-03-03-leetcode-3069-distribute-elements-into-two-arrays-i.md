---
layout      : single
title       : LeetCode 3069. Distribute Elements Into Two Arrays I
tags        : LeetCode Easy Array Simulation
---
周賽387。

## 題目

輸入索引由 1 開始，長度為 n 的整數陣列 nums。其中每個元素都是**不同**的。

你必須執行 n 次操作，將 nums 中的元素分配到 arr1 和 arr2 中。  
第一次操作，先將 nums[1] 加入 arr1。第二次操作，將 nums[2] 加入 arr2。  
之後第 i 次操作，則按照以下規則：  

- 若 arr1 的最後一個元素**大於** arr2 的最後一個元素，則將 nums[i] 加入 arr1  
- 否則將 nums[i] 加入 arr2  

陣列 result 是由 arr1 和 arr2 連接而成。  
例如：arr1 = [1,2,3], arr2 = [4,5,6]，則 result = [1,2,3,4,5,6]。  

回傳陣列 result。  

## 解法

按照題意模擬。  
題目保證 nums 中的元素都不同，因此不必考慮相等的情形。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        a1 = [nums[0]]
        a2 = [nums[1]]
        for i in range(2, N):
            x = nums[i]
            if a1[-1] > a2[-1]:
                a1.append(x)
            else:
                a2.append(x)
                
        return a1 + a2
```
