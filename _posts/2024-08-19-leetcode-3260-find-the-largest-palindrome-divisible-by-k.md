---
layout      : single
title       : LeetCode 3260. Find the Largest Palindrome Divisible by K
tags        : LeetCode Hard String DP DFS Greedy
---
weekly contest 411。  

## 題目

輸入兩個正整數 n 和 k。  

一個 **k 回文** 的整數 x 滿足：  

- x 是回文。  
- x 可被 k 整除。  

求**最大的** n 位數 **k 回文**，並以字串方式回傳。  

注意：不可有前導零。  

## 解法

每個**數位**要滿足特定餘數，並且**求極值**，根據經驗判斷是**數位 dp**。  
但是和以往做過的題型有些許差異，與其說是 dp，不如說更像是普通的 dfs。  

---

首先，當 ans[i] 填入某個數字 x 後，根據回文的限制，ans[n-1-i] 也必須填 x。  
因此只需要枚舉 n 的一半。注意 n 可能為奇數，所以必須**上取整**。  

再者，為了使答案盡可能大，越靠左的數字應該**貪心**地從 9 開始往 0 嘗試填入。**第一個找到的填法就是答案**。  
雖然題目規定不可有**前導零**，但肯定存在一個數 kk..kk 可以被 k 整除，故永遠不會有前導零。  

最後是餘數的部分，根據模運算的性質，有：  
> (a+b) % k  
> = a%k + b%k  

舉個例子：  
> n = 3  
> 假設 ans[0] = ans[2] 都填入 9  
> 相當於 sum[0..2] = (sum[1..1] + 900 + 9) % k  

餘數只需要像普通的**數位 dp** 以狀態表示即可。  

---

定義 dp(i, mod)：當前餘數為 mod 時，試填 ans[i] 和 ans[n-1-i] 是否合法。  
轉移：dp(i, mod) = any(dp(i+1, (mod+x) % k)) WHERE 0 <= x <= 9。  
base：當 i = ceil(n/2) 時，數字已填完。若餘數為 0 則回傳 true；否則回傳 false。  

時間複雜度 O(nkD)，其中 D = 10 種數字。  
空間複雜度 O(nk)。  

```python
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        exp = [1] * n
        for i in range(1, n):
            exp[i] = (exp[i-1] * 10 % k)

        half = (n+1) // 2
        ans = [""] * n
        
        @cache
        def dp(i, mod):
            # base case
            if i == half:
                return mod == 0

            # fill digits from 9 to 0
            # since kk...kk is always divisible by k
            # there won't be any leading zero
            for x in reversed(range(0, 10)):
                inc = x * exp[i]
                if i != n-1-i: # not center 
                    inc += x * exp[n-1-i]
                new_mod = (mod + inc) % k
                if dp(i+1, new_mod): # build answer 
                    ans[i] = ans[n-1-i] = str(x)
                    return True
            return False

        dp(0, 0)

        return "".join(ans)
```
