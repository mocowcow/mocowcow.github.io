---
layout      : single
title       : LeetCode 3129. Find All Possible Stable Binary Arrays I
tags        : LeetCode Medium Array DP
---
雙周賽 129。非常值得吐槽的一題。測資範圍非常奇妙，而且嚴重卡常數。  
最鳥的是：有些語言照著官方提示的做法也不能過。  

## 題目

輸入三個正整數 zero, one 和 limit。  

一個**穩定的**陣列 arr 滿足：  

- 數字 0 正好出現 zero 次  
- 數字 1 正好出現 one 次  
- 每個長度大於 limit 的子陣列必須擁有 0 和 1  

求有多少**穩定的**二進位陣列。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

先講講官方提示的做法，我比賽中也是這樣做，但是 py 不能過；golang 倒是可以。  

限制一個數最多連續出現 limit 次，就可以保證大於 limit 的子陣列擁有兩種數。  
在知道 0, 1 總數的情況下，就是以維護剩餘數量，並枚舉當前要填哪個。  
考慮到 limit，還得知道上一個數選了什麼，才有辦法計算連續次數。  

定義 dp(i, j, prev, cnt)：在 prev 已經連續出現 cnt 次的前提下，剩下 i 個 0 和 j 個 1 的填法。  
轉移：選 0 和選 1 加總。  

- 選 0，dp(i - 1, j, 0, new_cnt)。若 prev = 0 則 new_cnt = cnt + 1；否則 1  
- 選 1，dp(i, j - 1, 1, new_cnt)。若 prev = 1 則 new_cnt = cnt + 1；否則 1  

BASE：當 i 或 j 小於 0，或 cnt > limit，不合法回傳 0；否則 i, j = 0 剛好選完，回傳 1。  

時間複雜度 O(zero \* one \* limit)。  
空間複雜度 O(zero \* one \* limit)。  

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j, prev, cnt):
            if i < 0 or j < 0:
                return 0
            if cnt > limit:
                return 0
            if i == 0 and j == 0:
                return 1
            
            if prev == 0: # prev is 0
                res = dp(i - 1, j, 0, cnt + 1) # use 0
                res += dp(i, j - 1, 1, 1) # use 1
            else: # prev is 1
                res = dp(i - 1, j, 0, 1) # use 0
                res += dp(i, j - 1, 1, cnt + 1) # use 1
            return res % MOD
        
        ans = dp(zero - 1, one, 0, 1) + dp(zero, one - 1, 1, 1)
        
        return ans % MOD
```

基於**對稱性**，填各 (1, 3) 或 (3, 1) 個方案數是一樣的。  
可以使用第一個參數表示**上次選的數**，這樣就可以省略掉 prev。  

注意：記憶化沒清快取會 MLE。  
雖然複雜度不變，但常數至少減半，勉強能過了。  

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j, cnt): # prev is i
            if i < 0 or j < 0:
                return 0
            if cnt > limit:
                return 0
            if i == 0 and j == 0:
                return 1
            
            res = dp(i - 1, j, cnt + 1) # use i
            res += dp(j - 1, i, 1) # use j
            return res % MOD
        
        ans = dp(zero - 1, one, 1) + dp(one - 1, zero, 1)
        dp.cache_clear() # prevent MLE
        
        return ans % MOD
```

看到有人不是枚舉選哪個，而是交替枚舉**選多少個**。  
若當前輪到要選 1，則枚舉選的個數 1 <= x <= min(limit, j)。  

時空複雜度依然不變。但執行時間比上面兩種都快。  

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j, use):
            if i == 0 and j == 0:
                return 1
            
            res = 0
            if use == 0: # use 0
                for x in range(1, min(i, limit) + 1):
                    res += dp(i - x, j, 1)
            else: # use 1
                for x in range(1, min(j, limit) + 1):
                    res += dp(i, j - x, 0)
            return res % MOD
        
        ans = dp(zero, one, 0) + dp(zero, one, 1)
        
        return ans % MOD
```
