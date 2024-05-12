---
layout      : single
title       : LeetCode 3147. Taking Maximum Energy From the Mystic Dungeon
tags        : LeetCode Medium Array DP
---
周賽 397。

## 題目

在神秘的地牢中，有 n 個法師排成一線，這些法師會根據其能力直幫你補魔力。  
但有些法師會補**負數**的魔力，也就是扣你的魔。  

根據地牢的詛咒，每當你被第 i 個法師補魔，你就會立刻被傳送到第 (i + k) 個法師的位置。除非第 (i + k) 個法師不存在，則停止傳送。  
也就是說，你可以選擇一個出發點，並且一直被往後傳送，且從**所有經過的法師**身上補魔。

輸入陣列 energy 和 整數 k。求可獲得的最大魔力。  

## 解法

一開始還以為可以選擇要不要補。其實沒得選，法師一定會幫你好補滿。  

當你選擇在 i 出發，會立刻被傳送到 i + k，也就是在 i + k 出發的結果上再加上 energy[i]。  
有重疊的子問題，考慮 dp。  

定義 dp(i)：從 i 出發的最大魔力值。  
轉移：dp(i) = energy[i] + dp(i + k)  
base：當 i >= N，沒有法師，回傳 0。  

枚舉所有出發點，最大值就是答案。  

```python
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        
        @cache
        def dp(i):
            if i >= N:
                return 0
            return dp(i + k) + energy[i]
            
        ans = -inf
        for i in range(N):
            ans = max(ans, dp(i))
            
        return ans  
```
