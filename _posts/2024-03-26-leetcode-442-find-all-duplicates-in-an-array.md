---
layout      : single
title       : LeetCode 442. Find All Duplicates in an Array
tags        : LeetCode Medium Array HashTable Sorting
---
每日題。cycle sort 系列。

## 題目

輸入長度 n 的整數陣列 nums，所有整數都在 [1, n] 範圍之內。  
每一個整數只會出現**一次**或**兩次**。  
回傳一個陣列，包含所有出現**兩次**的整數。  

時間複雜度必須是 O(n)，且只使用 O(1) 額外空間。  

## 解法

廢話不多說，遍歷 nums，把整數 x 放到 nums[x - 1] 就對了，如果重複就先不管。  
排序後，遍歷第二次。如果 nums[i] 不是 i + 1，就代表 nums[i] 因為重複所以放到錯的位置，加入答案。  

時間複雜度 O(N)。  
空間複雜度 O(1)，答案空間不計入。  

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            while nums[i] != i + 1:
                j = nums[i] - 1
                # ignore dup
                if nums[j] == nums[i]: 
                    break
                    
                # swap nums[i] to nums[i - 1]
                nums[i], nums[j] = nums[j], nums[i]
                
        ans = []
        for i in range(N):
            if nums[i] != i + 1:
                ans.append(nums[i])
                
        return ans
```
