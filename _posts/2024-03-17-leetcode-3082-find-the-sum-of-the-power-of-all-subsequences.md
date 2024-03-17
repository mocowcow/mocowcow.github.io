---
layout      : single
title       : LeetCode 3082. Find the Sum of the Power of All Subsequences
tags        : LeetCode Hard Array DP
---
雙周賽 126。

## 題目

輸入長度 n 的整數陣列 nums，還有正整數 k。  

一個陣列的**力量值**等於其總和為 k 的子序列的數量。  

求 nums 所有子序列的**力量值總和**。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

這題有點妙，計算力量值本身就要找子序列。所有子序列的力量值相當於找**子序列的子序列**。  
看看 n <= 100，光是要生子序列的 2^n 都會超時，更別想子序列的子序列。  

---

與其暴力生成所有子序列，不如找找看那些總和為 k 的子序列會對答案**貢獻**幾次。  

舉個例子：  
> nums = [1,1,5], k = 5  

很明顯一定要包含 5，他的子序列才可能滿足 k。  
> [1,1,5], [1,_,5], [_,1,5], [_,_,5]  
> 這四個子序列分別都可以貢獻一個子序列 [5]  
> 答案 = 4  

再來看看範例 1：  
> nums = [1,2,3], k = 3  

[1,2] 和 [3] 都滿足 k。看看他們各出現幾次：  
> [1,2,3], [1,2,_] 各貢獻一次 [1,2]  
> [1,2,3], [1,_,3], [_,2,3], [_,_,3] 各貢獻一次 [3]  
> 答案 = 2 + 4 = 6  

好像發現了一點規律：如果有個長度為 size 的子序列滿足 k，則他的貢獻次數 = 2^(N - size)。  
更嚴謹地說，如果有一子序列 [x1,x2] 滿足 k，每多出一個數 xi，都會使得子序列的數量翻倍，而且他們都必定包含 [x1,x2]：  
> 最初 [x1,x2]  
> 加入 x3  
> [x1,x2,x3], [x1,x2,_]  
> 加入 x4  
> [x1,x2,x3,x4], [x1,x2,_,x4], [x1,x2,x3,_], [x1,x2,_,_]  
> ...

---

如此一來，問題就轉換成：  

- 找到長度 size，且滿足 k 的子序列有幾個  
- 根據 size 計算貢獻  

在 nums 中找特定總和的子序列是比較常見的問題。  
定義 dp(i, sm)：已選的子序列總和為 sm，在 nums[i..(N-1)] 有幾種選法可以滿足 k。  
我們同時需要知道已選的長度，因此要多個狀態，變成 dp(i, sm, size)。  

轉移：nums[i] 選或不選，兩個加起來。  

- 選 nums[i]：dp(i + 1, sm + nums[i], size + 1)  
- 不選 nums[i]：dp(i + 1, sm, size)  

BASE：當 i = N 且 sm = k 時，滿足條件，根據 cnt 計算貢獻次數；否則當 sm > k 或 i = N 時不合法，回傳 0。  

---

在沒有選擇元素的的情況下，在 nums[0..(N-1)] 中滿足 k 的子序列貢獻次數。  
答案入口就是 dp(0, 0, 0)。  

注意：乍看之下子序列總和可能很大，但是因為超過 k 的部分都直接剪枝掉，因此只會保留總和 0\~k 的狀態。  
而 i 和 size 最多為 n，複雜度 O(N^2 \* k)，最多 10^6 個狀態。  

時間複雜度 O(N^2 \* k)。  
空間複雜度 O(N^2 \* k)。  

```python
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        
        @cache
        def dp(i, sm, size):
            if i == N and sm == k:
                return 2 ** (N - size)
            
            if i == N or sm > k:
                return 0
            
            res = dp(i + 1, sm, size) # no take
            res += dp(i + 1, sm + nums[i], size + 1) # take
            return res % MOD
        
        ans = dp(0, 0, 0)
        dp.cache_clear()
        
        return ans % MOD
```
