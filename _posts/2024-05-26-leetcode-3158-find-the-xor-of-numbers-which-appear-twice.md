---
layout      : single
title       : LeetCode 3158. Find the XOR of Numbers Which Appear Twice
tags        : LeetCode Easy Array Simulation HashTable BitManipulation Bitmask
---
雙周賽 131。

## 題目

輸入陣列 nums，其中每個數只會出現**一次或兩次**。  

求所有**出現兩次**的數的 XOR 結果。若沒有數出現兩次，則回傳 0。  

## 解法

按照題意模擬，先統計次數，再求答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0
        for k, v in d.items():
            if v == 2:
                ans ^= k

        return ans
```

測資範圍不大，可以用 bitmask 記錄各數的出現狀態。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        for x in nums:
            if mask & (1 << x):
                ans ^= x
            mask |= (1 << x)
            
        return ans
```
