---
layout      : single
title       : LeetCode 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K
tags        : LeetCode Hard Math DP HashTable
---
weekly contest 444。  
複雜度也很怪的題，還真沒想到怎麼做。  

## 題目

<https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/description/>

## 解法

相似題 [3490. count beautiful numbers]({% post_url 2025-03-16-leetcode-3490-count-beautiful-numbers %})。  
在複雜度分析上有異曲同工之妙，都是受限於**乘積**。  

---

找 nums 的**非空**子序列，滿足**交錯和** = k，且**不超過 limit 的最大乘積**。  

我們先忽略 limit 的限制，單純考慮**交錯和** sm 以及**乘積** prod 的求法。  
對於每個 x = nums[i] 考慮**選或不選**：  

- 不選，跳到 nums[i+1]  
- 選  
  - 當前選的是第偶數個，sm 加 x，prod 乘 x。然後考慮 nums[i+1]  
  - 當前選的是第奇數個，sm 減 x，prod 乘 x。然後考慮 nums[i+1]  

對於不同的選法，有可能得到相同的 i, sm 和 prod。有**重疊的子問題**，考慮 dp。  
直到最後選完滿足 prod = k 才更新最大值。  

---

連乘很容易溢位，而且乘積不會變小，**乍看之下** prod 超過 limit 就可以直接 return。  

但這是不正確的，因為有個特殊例外：  
一旦序列選了一個 0，乘積永遠都是 0，必不超過 limit。此時只需要關注交錯和是否為 k。  

對於超過 limit 的乘積，實際上是多少都無所謂，反正他只是在著變成 0。  
因此 prod 和 limit + 1 取最小值，以節省狀態數。  

---

另外還要求子序列**非空**。  
只依靠 sm 和 prod 無法判斷是否已經選過元素，還需要多一個狀態 is_empty = True/False。  
同時滿足三項限制才合法。  

```python
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        N = len(nums)

        @cache
        def dp(i, sign, sm, prod, is_empty):
            if i == N:
                if not is_empty and sm == k and prod <= limit:
                    return prod
                return -1

            x = nums[i]
            # no take
            res = dp(i+1, sign, sm, prod, is_empty)
            # take
            new_prod = min(prod*x, limit+1)
            res = max(res, dp(i+1, -sign, sm+sign*x, new_prod, False))
            return res

        ans = dp(0, 1, 0, 1, True)
        dp.cache_clear()  # prevent MLE

        return ans
```
