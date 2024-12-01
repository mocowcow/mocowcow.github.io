---
layout      : single
title       : LeetCode 3371. Identify the Largest Outlier in an Array
tags        : LeetCode Medium HashTable
---
weekly contest 426。  
題目有點繞，多看幾次才懂。  

## 題目

輸入整數陣列 nums。  
陣列中有 n 個元素，且正好有 n - 2 個元素是**特別的**。  
剩下其中兩個元素中，其中一個等於所有**特別元素**的和，另一個元素是**異常值**。  

**異常值**並不屬於**特別元素**或是他們的和。  

求 nums 中可能的**最大異常值**。  

## 解法

設陣列和為 tot，特別元素和為 sp，異常值為 e。則有：  
> tot = sp + sp + e  

先用雜湊表統計所有元素頻率。  
然後枚舉 nums 中所有元素作為 e，試求 sp2 = tot - e。  
若 sp2 為偶數，且有表中還有出現 sp，則代表 e 可作為異常值，更新答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        tot = sum(nums)
        d = Counter(nums)
        ans = -inf
        for e in nums:
            d[e] -= 1
            sp2 = tot - e
            if sp2 % 2 == 0 and d[sp2//2] > 0:
                ans = max(ans, e)
            d[e] += 1

        return ans
```
