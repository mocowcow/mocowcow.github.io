---
layout      : single
title       : LeetCode 3334. Find the Maximum Factor Score of Array
tags        : LeetCode Medium Math Simulation PrefixSum
---
weekly contest 421。  
LCM 真的很麻煩，肯定很多人被煩死。  

## 題目

輸入整數陣列 nums。  

**因子分數**定義為陣列所有元素的 最小公倍數 (LCM) 與 最大公因數 (GCD) 的乘積。  

求**最多**移除一個元素後 nums 的**最大因子分數**。  

注意：單個數字的 LCM 和 GCD 都等於其本身，而**空陣列**的因子分數為 0。  

## 解法

測資範圍不大，暴力最方便。  
寫一個函數 f(j) 代表刪掉 nums[j] 的得分。  
注意答案也可以不刪，隨便代入一個無效索引即可。  

時間複雜度 O(N^2 \* log MX)，其中 MX = max(nums)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        
        def f(j):
            gcd_ = 0
            lcm_ = 1
            for i, x in enumerate(nums):
                if i != j:
                    gcd_ = gcd(gcd_, x)
                    lcm_ = lcm(lcm_, x)
            return gcd_ * lcm_
            
        return max(f(j) for j in range(N+1))
```

如果 nums 長一點就需要優化了。  

注意到 gcd, lcm 都有交換率和結合率，不在乎運算的順序。  
因此可以做**前後綴分解**。  
相似題 [238. product of array except self]({% post_url 2022-09-03-leetcode-238-product-of-array-except-self %})。  

時間複雜度 O(N log MX)，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        
        pre_gcd = [0] * N
        pre_lcm = [0] * N
        gcd_, lcm_ = 0, 1
        for i in range(N):
            gcd_ = gcd(gcd_, nums[i])
            lcm_ = lcm(lcm_, nums[i])
            pre_gcd[i] = gcd_
            pre_lcm[i] = lcm_

        suf_gcd = [0] * N
        suf_lcm = [0] * N
        gcd_, lcm_ = 0, 1
        for i in reversed(range(N)):
            gcd_ = gcd(gcd_, nums[i])
            lcm_ = lcm(lcm_, nums[i])
            suf_gcd[i] = gcd_
            suf_lcm[i] = lcm_

        ans = suf_gcd[0] * suf_lcm[0]
        for i in range(N):
            gcd_ = gcd((pre_gcd[i-1] if i > 0 else 0), (suf_gcd[i+1] if i+1 < N else 0))
            lcm_ = lcm((pre_lcm[i-1] if i > 0 else 1), (suf_lcm[i+1] if i+1 < N else 1))
            ans = max(ans, gcd_ * lcm_)

        return ans
```
