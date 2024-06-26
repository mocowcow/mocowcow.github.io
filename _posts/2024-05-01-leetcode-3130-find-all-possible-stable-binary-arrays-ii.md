---
layout      : single
title       : LeetCode 3130. Find All Possible Stable Binary Arrays II
tags        : LeetCode Hard Array DP PrefixSum
---
雙周賽 129。

## 題目

輸入三個正整數 zero, one 和 limit。  

一個**穩定的**陣列 arr 滿足：  

- 數字 0 正好出現 zero 次  
- 數字 1 正好出現 one 次  
- 每個長度大於 limit 的子陣列必須擁有 0 和 1  

求有多少**穩定的**二進位陣列。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

上一篇提到 dp(i, j, use) 需要枚舉當前數字**選多少個**，每個狀態需要枚舉 1\~ limit。  

例如 limit = 2 時：  
> dp(i, j, 0) 轉移 = dp(i - 1, j, 1) + dp(i - 2, j, 1)  
> dp(i - 1, j, 0) 轉移 = dp((i - 1) - 1, j, 1) + dp((i - 1) - 2, j, 1)  
> dp(i - 2, j, 0) 轉移 = dp((i - 2) - 1, j, 1) + dp((i - 2) - 2, j, 1)  

可以發現，對於相同的 j 來說，轉移來源會有部分重疊。  
這時可以用**前綴和**，將 O(limit) 的轉移優化成 O(1)。  

時間複雜度 O(zero \* one)。  
空間複雜度 O(zero \* one)。  

其實這樣複雜度應該是合格，無奈測資很兇，還是會超時。  

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j, use):
            if i == 0 and j == 0:
                return 1
            
            if use == 0: # use 0
                # for x in range(1, min(i, limit) + 1):
                #     res += dp(i - x, j, 1)
                res = ps(i - 1, j, 1) - ps(i - (limit + 1), j, 1)
            else: # use 1
                # for x in range(1, min(j, limit) + 1):
                #     res += dp(i, j - x, 0)
                res = ps(i, j - 1, 0) - ps(i, j - (limit + 1), 0)
            return res % MOD
        
        @cache
        def ps(i, j, use):
            if i < 0 or j < 0:
                return 0
            if use == 0: # sum for dp(i, j - x, 0)
                res = dp(i, j, 0) + ps(i, j - 1, 0)
            else: # sum for dp(i - x, j, 1)
                res = dp(i, j, 1) + ps(i - 1, j, 1)
            return res % MOD
        
        ans = dp(zero, one, 0) + dp(zero, one, 1)
        dp.cache_clear()
        ps.cache_clear()
        
        return ans % MOD
```

上一篇也提到，基於**對稱性**，可以省略掉參數 use。前綴和也是如此。  
雖然還是很慢，但至少能過了。  

遞推版本是真的難寫，等哪天我想通再回來補課。  

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j): # use i
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            # res = 0
            # for k in range(1, limit + 1):
            #     res += dp(j, i - k)
            res = ps(j, i - 1) - ps(j, i - (limit + 1)) # reverse (i - x, j) to (j, i - x)
            return res % MOD
          
        @cache
        def ps(i, j): # sum of dp(i, j) .. dp(i, 0)
            if j < 0:
                return 0
            res = dp(i, j) + ps(i, j - 1) 
            return res % MOD
        
        ans = dp(zero, one) + dp(one, zero)
        dp.cache_clear()
        ps.cache_clear()
        
        return ans % MOD
```

以下提供另一種思路，但解釋的很爛，請注意。  

因為受到 limit 的約束，在 dp 時需要帶一個參數 cnt 來代表連續的次數，才能得知那些選擇不合法。  
但是當 zeor, one <= 1000，光是這兩個的狀態數就高達 N^2，再加上 cnt 肯定沒戲。得想辦法優化掉。  

先來看看不帶 cnt 會多算那些不合法的東西。  
根據定義，dp(i, j, use) 是指當前最後一個數選擇 use 的**合法方案** (第 i + j 個數選 use)。  
既然這些方案是合法的，那他必然要從**合法的子問題**中轉移而來。也就是說，先前的 (i + j - 1) 個數中，最多連續出現 limit 次的相同字元。  

以 limit = 2, dp(3, 1, 0) 為例。  
當前必須選擇 0，而先前的數可能是 0 或 1 結尾。轉移來源有：  
> 以 0 結尾的 dp(2, 1, 0) 有：  
> 010, 100  
> 以 1 結尾的 dp(2, 1, 1) 有：  
> 001  

當前要選的是 0，所以從 1 結尾的方案轉移過來肯定沒問題，反正兩個數不同。  
從 0 轉移就有點問題：  
> 010 變成 0100 合法  
> 100 變成 1000 **不合法**  

---

想了好久，終於想出個自己能夠接受的解釋。  

首先想清楚 dp(i, j, 0) 的定義是什麼？  
填 i 個 0 和 j 個 1 ，且最多連續 limit 次的**合法方案數**。而且最後一個數是選 0。  
> xxx0  

如果從 dp(i - 1, j, k=0/1) 轉移到 dp(i, j, 0) 代表著什麼？  
從填 i - 1 個 0 和 j 個 1 的**所有合法方案**中，在最後面加上一個 0。  
> xx00  
> xx10  

dp(i - 1, j, k=0/1) 又會從各自來源轉移。以此類推，直到數字用完為止。  
> x000  
> x010  
> x100  
> x110  

---

dp(i, j) 的定義是**合法方案數**，這很重要所以一直重複講！！

再次回到 limit = 2, dp(3, 1, 0) 的例子。  
其轉移來源 dp(2, 1, 0) 的**合法方案**有：  
> 010, 100  

其中 100 會轉移過去之後會變成非法，因為他連續超過 limit 次。  
如果 dp(i - 1, j) 是 dp(i, j) 填了一個 0 的方案數，那麼 dp(i, j) 填了 (limit + 1) 個 0 的方案數就是 dp(i - (limit + 1), j)。  
既然已經知道這樣填不合法，那直接把他扣掉就行。  

時間複雜度 O(zero \* one)。  
空間複雜度 O(zero \* one)。  

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j, use):
            if i < 0 or j < 0:
                return 0
            
            if i == 0:
                if use == 1 and j <= limit:
                    return 1
                else:
                    return 0
                
            if j == 0:
                if use == 0 and i <= limit:
                    return 1
                else:
                    return 0
            
            if use == 0: # use 0 
                res = dp(i - 1, j, 0) + dp(i - 1, j, 1) 
                res -= dp(i - (limit + 1), j, 1) # no more than limit 
            else: # use 1
                res = dp(i, j - 1, 0) + dp(i, j - 1, 1)
                res -= dp(i, j - (limit + 1), 0) # no more than limit 
            return res % MOD
        
        ans = dp(zero, one, 0) + dp(zero, one, 1)
        dp.cache_clear()
        
        return ans % MOD
```
