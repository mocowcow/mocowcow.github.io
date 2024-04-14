---
layout      : single
title       : LeetCode 3117. Minimum Sum of Values by Dividing Array
tags        : LeetCode Hard Array DP BitManipulation
---
周賽 393。這題也很妙，剛開始想了個很普通的 DP 解法，掐指一算複雜度好像不太對就沒寫了。沒想到竟然是正解，虧大了。  

## 題目

輸入兩個長度分別為 n, m 的整數陣列 nums 和 andValues。  

一個陣列的**價值**等於其最後一個元素。  

你必須將 nums 分割成 m 個**不相交**且**連續**的子陣列。  
其中第 i 個子陣列的邊界為 [l<sub>i</sub>, r<sub>i</sub>]，且子陣列所有元素做位元 AND 的結果等於 andValues[i]。  

求成功分割成 m 個滿足條件的子陣列，其**最小價值**是多少。若不能分割，則回傳 -1。  

## 解法

首先複習 AND 運算的特性：**只少不多**。做越多次運算，越可能使結果值變小。  
如果當前的子陣列 AND 結果小於 andValues[i]，不管怎樣都沒救了，可以直接跳過。  

---

經典的劃分型 DP。枚舉分割點 i，可以選擇**分割**或**不分割**。  
為了判斷能不能分割，我們需要維護**當前子陣列的 AND 結果**val。  
當然還要**已分割的子陣列數量** j。  

定義 dp(i, j, val)：且當前子陣列 AND 值為 val，繼續從子陣列 nums[i..N-1] 中，分割出 m - j 個不相交子陣列的最小價值。  
轉移：dp(i, j, val) = min(分割, 不分割)  

- 不分割 = dp(i + 1, j, val)
- 分割 = min(res, dp(i + 1, j + 1, -1) + nums[i])

BASE:當 i = N 且 j = M 時，正好分割成功，回傳 0；否則只有其中一項滿足時，則代表不合法狀況，回傳 inf。  
另外就是剛才提到的，如果 val 小於 andValues[i]，可以提早剪枝回傳 inf。  

---

這時間複雜度不太直觀。  

分割點 i 有 N = 10^4 個，沒問題。  
子陣列個數 j = M = 10 個，也沒問題。  
那 AND 結果值 val 乍看之下好像高達 N 個。怎麼看都會超時，問題可大了。  

再次回想剛才說過 AND 運算的特性：**只少不多**。  
每次對子陣列加入新的元素、進行 AND 運算後，只有兩種可能：  

1. val 不變  
2. val 減少，而且至少有一個位元從 1 變成 0  

而 nums[i] 最大只能到 MX = 10^5，大約 17 個位元。  
每次至少會失去 1 個設置位元，所以對於以同一個 nums[i] 作為結尾的子陣列來說，最多只能得到 17 種 val 的值。  

時間複雜度 O(NM log MX)，其中 MX = max(nums[i])。  
空間複雜度 O(NM log MX)。  

```python
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        N, M = len(nums), len(andValues)
        
        @cache
        def dp(i, j, val):
            if i == N and j == M:
                return 0

            if i == N or j == M:
                return inf

            val &= nums[i] # add to current subarray
            if val < andValues[j]: # pruning, val cannot be larger
                return inf

            res = dp(i + 1, j, val) # no split
            if val == andValues[j]: # split
                res = min(res, dp(i + 1, j + 1, -1) + nums[i])
            return res
        
        ans = dp(0, 0, -1)
        
        if ans == inf:
            return -1
        
        return ans
```
