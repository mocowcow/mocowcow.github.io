---
layout      : single
title       : LeetCode 3352. Count K-Reducible Numbers Less Than N
tags        : LeetCode Hard DP
---
weekly contest 423。  
在奇怪的小地方卡很久，難點倒是沒卡，略尷尬。  

## 題目

輸入二進位字串 s，代表數字 n 的二進制。  
另外輸入整數 k。  

若一個整數 x 可以透過**至多** k 次操作變成 1，則稱其為**k 可約**的：  

- 將 x 替換成其二進制中的置位 (set bit) 數。  

例如：6 的二進制是 "110"。操作一次後變成 2，因為 "110" 有 2 個置位。  
2 再操作一次後變成 1，因為 "10" 有 1 個置位。  

求有多少**小於** n 的整數是**k 可約**的。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

首先不管 k 多少，一個整數 x 變成 1 的所需操作次數都是不變的。  
但 s 長度高達 800，共有 2^800 個數，不可能全部算出來。  

注意到操作次是根據置位數而定，例如就是說 "100...00" 和 "000...01" 所需的操作次數相同。  
我們可以根據置位數來求操作次數。  
定義 ops[i]：有 i 個置位時，變成 1 所需要的操作次數。  

這些整數的置位至少 1 個、至多 800 個，先預處理所有可能。  

注意：ops[1] 對應的二進制有 "1", "10", "100" 等，其中只有 "1" 不需操作，其餘都需要 1 次操作才能變成 "1"。  
但是本題中 k >= 1，所以設 ops[1] = 1 也不會影響 "1" 對答案的貢獻，因此不需特判。  

---

剩下只要以 s 為限制，找到所有滿足條件的填法，也就是 [1, n-1] 之間有多少合法的數。  
老同學不難想到**數位 dp**。  

狀態需要當前選填位置的 i，還有是否受限於 s 的 is_limit。  
還需要以制位個數判斷是否合法，因此還要一個 cnt1。  

定義 dp(i, is_limit, cnt1)：當前有 cnt1 個制位、是否受限於 s，且索引 i 之後的數字有多少填法不超過 k 次操作。  
轉移：sum( dp(i+1, new_limit, new_cnt1) )，根據 is_limit 決定此位能選填的數。  
base：當 i = N 時，判斷 ops[cnt1] 是否不超過 k，若合法回傳 1，否則回傳 0。  

---

答案入口為 dp(0, True, 0)。這包含了 [0, n] 之間的**k 可約**個數。  
但是整數 0 不管幾次操作都不可能變成 0，所以要從答案中扣掉 1 (也可以直接規定 ops[0] = inf)。  
並且題目要求**小於** n，所以 n 也不合法。特判 n 若合法，答案也要再扣掉 1。  

時間複雜度 O(N^2)，其中 N = len(s)，並非 s 對應的整數。  
空間複雜度 O(N^2)。  

```python
MOD = 10 ** 9 + 7
MX = 800 + 5

# ops[i]: the times a element which has i set bits need to reduce
# ops[1] include "1", "10", "100", ..
# only "1" takes no op, others take 1 op
ops = [0] * MX
for i in range(1, MX): 
    ops[i] = ops[i.bit_count()] + 1

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        N = len(s)

        @cache
        def dp(i, is_limit, cnt1):
            if i == N:
                return int(ops[cnt1] <= k)
            res = 0
            down = 0
            up = 1 if not is_limit else int(s[i])
            for j in range(down, up + 1):
                new_cnt1 = cnt1 + j
                new_limit = is_limit and j == up
                res += dp(i + 1, new_limit, new_cnt1)
            return res % MOD

        ans = dp(0, True, 0) 
        dp.cache_clear() # prevent MLE
        
        # exclude empty string
        ans -= 1

        # exclude s
        s_cnt1 = s.count("1")
        if ops[s_cnt1] <= k:
            ans -= 1
        
        return ans % MOD
```
