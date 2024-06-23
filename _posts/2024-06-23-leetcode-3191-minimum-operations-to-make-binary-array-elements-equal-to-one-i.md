---
layout      : single
title       : LeetCode 3191. Minimum Operations to Make Binary Array Elements Equal to One I
tags        : LeetCode Medium Array Greedy Simulation
---
雙周賽 133。

## 題目

輸入二進位整數陣列 nums。  

你可以執行以下操作任意次：  

- 選擇三個連續的元素並反轉  

反轉指把 0 變成 1，或是把 1 變成 0。  

求**最少**需要幾次操作，才能使得所有元素變成 1。若不可能則回傳 -1。  

## 解法

對於 nums[i] 來說，為了避免被後續操作影響，必須依照由左到右的方向檢查。  
只要 nums[i] 不為 0，則反轉 nums[i..(i+2)] 區間。  
但最後的 nums[N - 2] 和 nums[N - 1] 兩個位置無法單獨反轉，只要他們不為 0，則答案為 -1。  

每次只需要反轉三個，可以視作比較小的常數。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N - 2):
            if nums[i] == 0:
                ans += 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        
        if nums[-1] + nums[-2] != 2:
            return -1
        
        return ans
```

那如果不是 3 個元素，而是 k 個的話，則要考慮支持區間修改的資料結構，例如線段樹或是差分。  
以下使用差分。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        k = 3
        diff = [0] * (N + k)
        ps = 0
        ans = 0
        for i in range(N - k + 1):
            ps ^= diff[i]
            if nums[i] ^ ps == 0:
                ans += 1
                ps ^= 1
                diff[i + k] ^= 1
        
        # cant flip
        for i in range(N - k + 1, N):
            ps ^= diff[i]
            if nums[i] ^ ps == 0:
                return -1
        
        return ans
```
