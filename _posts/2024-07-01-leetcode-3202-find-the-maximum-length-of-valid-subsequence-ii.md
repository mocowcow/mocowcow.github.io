---
layout      : single
title       : LeetCode 3202. Find the Maximum Length of Valid Subsequence II
tags        : LeetCode Medium Array DP
---
周賽 404。

## 題目

輸入整數陣列 nums，還有整數 k。  

nums 的長度為 x 的**有效**子序列 sub 滿足：  

- (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k  

求 nums 的**最長的有效子序列**。  

## 解法

和前一題相同，子序列的奇偶項要同餘。  
不同的是這次是模 k，所以餘數會有 k = 1000 種。  
設子序列的餘數為 x, y 交替，光是枚舉所有組合就高達 10^6 種，有點微妙。  

這種子序列問題通常可以使用 dp，根據前一項選了什麼元素，來決定當前元素**選或不選**。  
我們必須知道是哪兩種餘數交替，所以 x, y 必須在 dp 狀態參數之中。  

定義 dp(i, x, y)：在 nums[i..n-1] 的 x, y 交替最長子序列長度，且下一個元素必須餘 x。  
轉移：  

- 若 nums[i] % k == x，可選 nums[i]，下一個元素要餘 y：  
    dp(i, x, y) = dp(i + 1, y, x) + 1  
- 若 nums[i] % k != x，略過 nums[i]：  
    dp(i, x, y) = dp(i + 1, x, y)  

base：當 i = N，沒有剩餘元素，回傳 0。  

---

雖然轉移是 O(1)，但狀態數高達 10^9，還是超時。需要想辦法優化。  

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums = [x % k for x in nums]
        
        @cache
        def dp(i, x, y):
            if i == N:
                return 0
            if nums[i] == x:
                return dp(i + 1, y, x) + 1
            else:
                return dp(i + 1, x, y)
            
        ans = 0
        for x in range(k):
            for y in range(k):
                ans = max(ans, dp(0, x, y))
                
        return ans
```
