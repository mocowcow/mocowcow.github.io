---
layout      : single
title       : LeetCode 3584. Maximum Product of First and Last Elements of a Subsequence
tags        : LeetCode Medium SlidingWindow TwoPointers Greedy
---
weekly contest 454。

## 題目

<https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/description/>

## 解法

範例 1 很好心告訴我們 m = 1 時特判答案為各元素平方的最大值。  

---

討論 m >= 2 的情況：  
子序列長的像是 [first, #,.. #, last]，頭尾中間需要填充 m-2 個元素。  
初步想法是滑窗枚舉中間 m-2 **不能選的元素**，然後從左右邊剩餘元素找最大乘積。  
但是好像有點麻煩。  

轉換思路，改成**枚舉 last**，若左方剩餘超過 m-2 個元素，則加入 first 的候選名單中。  
根據 last 的值決定 fisrt 的值：  

- last > 0，first 必 > 0  
- last < 0，first 必 < 0  

所以我們只需要維護 first 的最大最小值即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1:
            return max(x*x for x in nums)

        mn, mx = inf, -inf
        ans = -inf
        for i, x in enumerate(nums):
            if i > m-2:
                y = nums[i-m+1]
                mn = min(mn, y)
                mx = max(mx, y)
                if x < 0:
                    ans = max(ans, x*mn)
                else:
                    ans = max(ans, x*mx)

        return ans
```
