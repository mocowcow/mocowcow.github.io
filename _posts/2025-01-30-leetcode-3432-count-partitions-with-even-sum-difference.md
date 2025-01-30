---
layout      : single
title       : LeetCode 3432. Count Partitions with Even Sum Difference
tags        : LeetCode Easy Simulation PrefixSum Math
---
weekly contest-434。

## 題目

<https://leetcode.com/problems/count-partitions-with-even-sum-difference/>

## 解法

長度 N 的陣列切成兩個**非空**子陣列，有 N-1 種切法。  

設左右子陣列和分別為 l, r。  
當 l 增加 x，則 r 會減少 x。  
枚舉所有子陣列切法，若絕對差為偶數則答案加 1。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = sum(nums)
        for x in nums[:-1]:
            l += x
            r-= x
            if abs(l-r) % 2 == 0:
                ans += 1

        return ans
```

答案是求滿足 (l-r) % 2 == 0 的次數。  

> s = l+r 變形得到 s-l = r  
> 代入 l-r 得到 l-(s-l)
> 整理得到 2l - s  

因為 2l 肯定是偶數，所以只要 s 同為偶數，那切出來的 N-1 種 (l-r) 肯定也是偶數。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums)-1 if sum(nums) % 2 == 0 else 0
```
