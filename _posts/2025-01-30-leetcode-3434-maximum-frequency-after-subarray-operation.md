---
layout      : single
title       : LeetCode 3434. Maximum Frequency After Subarray Operation
tags        : LeetCode Medium Greedy DP
---
weekly contest-434。

## 題目

<https://leetcode.com/problems/maximum-frequency-after-subarray-operation/>

## 解法

可以選一段子陣列，對每個元素加上 x。  
此操作等價於**子陣列中所有元素 t 變成目標值 k**，但子陣列中**原本的 k 會消失**。  

為了使 k 的次數最大化，要找到滿足 extra = sub.count(k) - sub.count(t) 最大值的子陣列 sub。  
最終答案就是 nums.count(k) - extra。  

---

我們不知道 t 選誰好，只能暴力枚舉所有可能性，反正至多只有 50 種。  
但還是需要 O(N) 時間內求出 t 的最大 extra。  

碰到 k 會使 extra 減 1；碰到 t 會使 extra 加 1；其餘元素不影響。  
要找到**子陣列**使得 extra 最大化，這正是 **kadane maximum subarray**。  
直接枚舉 t，各跑一次 kadane 就行了。  

注意：kadane 實作細節要注意判斷的順序，否則在 t=k 時會出現錯誤答案。  
最安全的方式是 t=k 時直接跳過。  

---

時間複雜度 O(N \* MX)，其中 MX 為 nums 中不同的元素個數。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        def kadane(target):
            mx = 0
            extra = 0
            for x in nums:
                if x == k:
                    extra -= 1
                elif x == t:
                    extra += 1
                if extra < 0:
                    extra = 0
                mx = max(mx, extra)
            return mx

        ans = 0
        for t in set(nums):
            ans = max(ans, kadane(t))

        return nums.count(k) + ans
```
