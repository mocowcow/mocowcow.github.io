---
layout      : single
title       : LeetCode 3290. Maximum Multiplication Score
tags        : LeetCode Medium DP
---
weekly contest 415。  
比賽中能過的代碼，賽後又加了幾個測資，現在又變成 MLE。  
不知道會不會被 rejudge 掉。  

## 題目

輸入長度 4 的整數陣列 a，以及長度**至少 4**的整數陣列 b。  

你必需從 b 之中選擇四個索引 i0, i1, i2 和 i3，滿足 i0 < i1 < i2 < i3。  
並獲得分數等於 a[0] \* b[i0] + a[1] \* b[i1] + a[2] \* b [i2] + a[3] \* b[i3]。  

求**最大**得分。  

## 解法

要在 b 之間找四個元素和 a 配對，而且順序有要求，所以要從固定往一個方向找。  
此處以 a[0], a[1], a[2], a[3] 的順序配對。  

遍歷 b 中每個元素 b[j]，嘗試和 a[i] 配對並決定**選或不選**。  
不同的選法可能導致 b 和 a 剩餘相同的元素，有**重疊的子問題**，因此考慮 dp。  

定義 dp(i, j)：配對 a[i..3] 和 b[j..N-1] 的最大得分，並決定 a[i] 是否和 b[j] 配對。  
轉移：dp(i, j) = max(選, 不選)。

- 選：dp(i+1, j+1)  
- 不選：dp(i, j+1)  

base：當 i = 4 時，代表 a 已經配對完，回傳 0；否則當 j = N 時，代表 a 還沒配完，但 b 已經沒了，不合法所以回傳 -inf。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        N = len(b)

        @cache
        def dp(i, j): # a[i], b[j]
            if i == 4:
                return 0
            if j == N:
                return -inf
            return max(
                dp(i, j+1), 
                dp(i+1, j+1) + a[i] * b[j]
            )

        ans = dp(0, 0)
        dp.cache_clear() # prevent MLE

        return ans
```
