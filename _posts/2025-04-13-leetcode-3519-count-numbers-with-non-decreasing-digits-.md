---
layout      : single
title       : LeetCode 3519. Count Numbers with Non-Decreasing Digits 
tags        : LeetCode Hard Math DP
---
weekly contest 445。  
第一次看到讓 C++ 吃鱉的題，因為沒有內建 big number，有點難搞。  

## 題目

<https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/description/>

## 解法

在很大的區間 [L,R] 求個數，不難想到**數位 dp**。  

但是數位 dp 是逐位填數字的，要怎麼知道最終結果的每個數位是**非遞減**？  
其實很簡單，只要多一個狀態表示上次填的數 last，然後本次填的數從 last 開始往上枚舉就行。  

根據排容原理，[L,R] 的答案即 [1,R] 扣掉 [1,L-1]。  

---

但還要先把 [L, R] 轉成轉換成 **b 進制**。  
相似題 [504. Base 7](https://leetcode.com/problems/base-7/description/)。  

進制轉換就是不斷求餘數的過程，勢必把區間 R 轉成整數後才能求餘。  
這時候 python 就很爽：我家很大，直接轉沒問題的。  

時間複雜度 O(N \* b^2)。  
空間複雜度 O(N \* b)。  

```python
MOD = 10 ** 9 + 7

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:

        def solve(s):
            N = len(s)

            @cache
            def dp(i, is_limit, last):
                if i == N:
                    return 1
                res = 0
                down = last
                up = b-1 if not is_limit else int(s[i])
                for j in range(down, up + 1):
                    new_limit = is_limit and j == up
                    res += dp(i + 1, new_limit, j)
                return res % MOD

            return dp(0, True, 0)

        nl = convertToBase(int(l)-1, b)
        nr = convertToBase(int(r), b)
        ans = solve(nr) - solve(nl)

        return ans % MOD


def convertToBase(x, b):
    res = []
    while x > 0:
        r = x % b
        res.append(str(r))
        x //= b
    res.reverse()
    return "".join(res)
```
