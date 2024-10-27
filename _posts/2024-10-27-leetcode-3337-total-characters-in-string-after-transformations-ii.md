---
layout      : single
title       : LeetCode 3337. Total Characters in String After Transformations II
tags        : LeetCode Hard DP Math Matrix
---
weekly contest 421。  
又是 dp，一場比賽 dp 三次，純度很高。  
雖然這大概不是面試會考的東西，但我剛好會，撿了個一百名。  

## 題目

輸入字串 s 和 整數 t，代表**轉換**次數，還有長度 26 的整數陣列 nums。  
每次**轉換**須按照以下規則替換字元：  

- 將字元 s[i] 替換成字母表後 nums[s[i] - 'a'] 個連續字母。  
    例如 s[i] = 'a' 且 nums[0] = 3，則 'a' 變成 "bcd"。  
- 若轉換超過 'z'，則**回頭**從 'a' 繼續。  
    例如 s[i] = 'y' 且 nums[24] = 3，則 'y' 變成 "zab"。  

求字串進行**正好** t 次**轉換**後的長度。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

相似題 [2851. string transformation]({% post_url 2023-09-12-leetcode-2851-string-transformation %})。  

基本上和 Q2 差不多，只是轉移方程不同，還有 t 變得超大。  
但 t = 1e15 真的有夠大，不給他加個 log 肯定過不去。  

在 Q2 的時候有講到這是一種**線性 dp**，每次轉移都可以看做一次**矩陣乘法**，因此可以用**矩陣快速冪**優化轉移過程。  
主要分成三個步驟：  

1. 統計 s 中各字元的頻率，構造初始矩陣 f0。  
2. 根據 nums 構造轉移矩陣 trans，也就是每次轉移字元c 會產生的其他字元個數。  
3. 用快速冪求 trans^t，乘上 f0，再統計各字元頻率。  

時間複雜度 O(N + 26^3 log t)。  
空間複雜度 O(26^2)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # initial state
        f0 = [[0]*26 for _ in range(26)]
        for c in s:
            f0[ord(c)-97][0] += 1

        # build transition matrix
        trans = [[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(nums[i]):
                trans[(i+j+1) % 26][i] += 1

        # apply transition t-times by fast power
        trans = mat_pow(trans, t)  
        res = mat_mul(trans, f0)
        return sum(res[i][0] for i in range(26)) % MOD


def mat_pow(base, p):
    # identity matrix
    res = [[0]*26 for _ in range(26)]
    for i in range(26):
        res[i][i] = 1
    while p > 0:
        if p & 1:
            res = mat_mul(res, base)
        p >>= 1
        base = mat_mul(base, base)
    return res


def mat_mul(a, b):
    c = [[0]*26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            for k in range(26):
                c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= MOD
    return c
```
