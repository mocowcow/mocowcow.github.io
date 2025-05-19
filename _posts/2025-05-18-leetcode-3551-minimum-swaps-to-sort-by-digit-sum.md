---
layout      : single
title       : LeetCode 3551. Minimum Swaps to Sort by Digit Sum
tags        : LeetCode Medium Simulation Sorting HashTable
---
weekly contest 450。  
本次寫起來最難受的一題，換來換去腦子差點打結。  

## 題目

<https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/>

## 解法

首先按題目要求排序 nums，將排序後的結果記做 target。  
逐一檢查每個位置 nums[i]，查看是否與 target[i] 相同：  

- 相同，不需操作  
- 不同，則找到 target[i] 當前位置 j，把 nums[i], nums[j] 交換  

需要快速查找某個元素 val 當前位於 nums 的位置。  
建立映射表 pos，其中 pos[val] = j，代表 pos 位於 nums[j]。  
每次換位 nums[j] 的值會改變，記得要更新映射表。  

時間複雜度 O((N log MX) + (N log MX))，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        # expected pos of val after sorting
        target = [[sum(int(c) for c in str(val)), val] for val in nums]
        target = [x[1] for x in sorted(target)]

        # current pos of val
        pos = {}
        for i, val in enumerate(nums):
            pos[val] = i

        # swap val to target pos
        ans = 0
        for i in range(N):
            t = target[i]
            # swap
            if nums[i] != t:
                ans += 1
                # t at nums[j]
                j = pos[t]
                # swap i,j then update mapping
                nums[i], nums[j] = nums[j], nums[i]
                pos[nums[i]] = i
                pos[nums[j]] = j

        return ans
```
