---
layout      : single
title       : LeetCode 3469. Find Minimum Cost to Remove Array Elements
tags        : LeetCode Medium DP
---
biweekly contest 151。  
這題挺奇妙的，除了測資很爛，記憶化會卡 MLE 以外，算是不錯的題。  

## 題目

<https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/description/>

## 解法

從元素 a, b, c 元素中選兩個，有三種選法：  

- 選 a, b，成本 max(a, b)  
- 選 a, c，成本 max(a, c)  
- 選 b, c，成本 max(b, c)  

直覺會認為選**最大**和**次大**的兩個最划算。但是範例 2 給出反例：  
> nums = [2,1,3,3]  
> 選 2,3 成本 3，變成 [1,3]  
> 選 1,3 成本 3，變成 []  
> 總成本 6  

正確方案是：  
> nums = [2,1,3,3]  
> 選 2,1 成本 2，變成 [3,3]  
> 選 3,3 成本 3，變成 []
> 總成本 5  

可見沒有固定的選擇規律。  
需要暴力枚舉所有可能的選法，考慮 dp。  

---

至於 dp 狀態的定義就很有趣了。  
假設我們每次選擇最靠左的兩個數，很明顯縮減成規模更小的子問題：  
> nums = [1,2,3,4,5,..]  
> 選 1,2 變成 [3,4,5,..]
> 選 3,4 變成 [5,..]

確定需要狀態 i 代表 nums[i..] 的最小成本。  

但如果不照順序選呢？  
> nums = [1,2,3,4,5,..]  
> 選 2,3 變成 [1,4,5,..]  
> 選 1,5 變成 [4,..]  

剩下的子問題可能**不是 nums 的子陣列**。  
但是**最多只會留下一個**。  
因此需要多一個狀態 pre 代表 nums[i..] 之前多的那個數。  

---

定義 dp(i, pre)： 刪除 [pre] + nums[i..] 的最小成本。  

我一開始是以 pre = 0 當作沒有剩餘，pre > 0 代表有剩餘，分成兩種狀況討論。  
後來發現很多高手的寫法更簡潔：就算沒有剩餘，也只要拿最前方的數當作 pre，就可以歸納成同一種情形。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def minCost(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dp(i, pre):
            if N - i < 2:
                return max([pre] + nums[i:i+2])
            
            a, b, c = pre, nums[i], nums[i+1]
            return min(
                dp(i+2, c) + max(a, b), 
                dp(i+2, b) + max(a, c), 
                dp(i+2, a) + max(b, c),
                )

        ans = dp(1, nums[0])
        dp.cache_clear() # prevent MLE
        
        return ans
```
