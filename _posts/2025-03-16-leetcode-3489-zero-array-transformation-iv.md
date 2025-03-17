---
layout      : single
title       : LeetCode 3489. Zero Array Transformation IV
tags        : LeetCode Medium DP
---
weekly contest 441。  
被 hidden case 騙到，太苦了。  

## 題目

<https://leetcode.com/problems/zero-array-transformation-iv/description/>

## 解法

先考慮 nums 只有一個元素的情形，通過考慮每個查詢的 val **選或不選**，組成 nums[i]。  
每個 nums[i] 都是獨立的，問題轉換成：  
> 按照查詢對每個 nums[i] 做 0/1 背包，滿足所有 nums[i] 的最少查詢數。  

---

先特判：nums 初始值全為 0，不須修改，答案 0。  
否則依序執行 queries[i]，若執行後可滿足條件，則回傳 i + 1。  

用集合 s 維護能組成的數，最初只有 0。  
每次代入 val，有兩種選擇：  

- 不選 val，集合不變。  
- 選 val，增加 x + val。其中 x 為 s 中的所有元素。  

例如：  
> s = {0}  
> 代入 val = 5  
> s2 = {0+5}  
> s = s + s2 = {0,5}  
> 代入 val = 3  
> s2 = {0+3, 5+3}  
> s = s + s2 = {0,3,5,8}  

記得 s 要先複製一份，避免在遍歷過程中修改。  

時間複雜度 O(N \* MX \* Q)。其中 MX = nums[i] 最大值。  
空間複雜度 O(N \* MX)。  

老實說 O(N \* MX \* Q) 算起來 10 \* 10^3 \* 10^3，高達 10^7。  
我一直猶豫這會不會過，看來這次測資很良心。  

```python
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        Q = len(queries)
        
        if sum(nums) == 0:
            return 0
        
        dp = [set() for _ in range(N)]
        for i in range(N):
            dp[i].add(0)

        for qi, (l, r, val) in enumerate(queries):
            for i in range(l, r+1):
                s = dp[i]
                for x in s.copy():
                    if x + val <= nums[i]:
                        s.add(x + val)

            # check
            if all(nums[i] in dp[i] for i in range(N)):
                return qi + 1

        return -1
```
