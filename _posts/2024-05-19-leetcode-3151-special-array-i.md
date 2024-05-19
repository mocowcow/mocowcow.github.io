---
layout      : single
title       : LeetCode 3151. Special Array I
tags        : LeetCode Easy Array Simulation
---
周賽 398。

## 題目

若陣列中每一對相鄰元素都是由奇偶性不同的數組成，則稱為**特殊的**。  

輸入整數陣列 nums。若 nums 是特殊陣列則回傳 true，否則回傳 false。  

## 解法

長度 N 的陣列會有 N - 1 組相鄰數對，逐一檢查即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(1, N):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        
        return True
```

py 一行版本。  

```python
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(a % 2 != b % 2 for a, b in pairwise(nums))
```
