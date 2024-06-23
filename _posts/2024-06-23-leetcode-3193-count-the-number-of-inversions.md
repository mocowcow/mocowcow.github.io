---
layout      : single
title       : LeetCode 3193. Count the Number of Inversions
tags        : LeetCode Hard Array DP
---
雙周賽 133。根據經驗來講，這題應該頂多 500 人過。結果有 1800 人過了，不愧是雙周賽，非常魔幻。  

## 題目

輸入整數 n 和二維整數陣列 requirements，其中 requirements[i] = [end<sub>i</sub>, cnt<sub>i</sub>]，代表以前綴的最後一個索引，以及其**逆序對**的數量。  

一個索引數對 (i, j) 若滿足以下條件，則稱為**逆序對**：  

- i < j 且 nums[i] > nums[j]  

求數列 [0, 1, 2, ..., n - 1] 的排列中，有多少種排列**滿足所有**requirements[i]，也就是 perm[0..end<sub>i</sub>] 正好擁有 cnt<sub>i</sub> 個**逆順對**。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

題目是求**前綴**的逆序對數量，因此考慮在已有的數列 prem 末端加入新的數會有什麼影響。  
假設 perm = [2,0]，在末端加上 1 之後，產生了一個逆序對 (nums[0] = 2, nums[2] = 1)。  
每加入一個數 x 後，產生的逆序對數量等於左方大於 x 的數個數。  

為了計算增加的逆序對，需要維護左方有哪些數出現過 (同時也知道那些還沒出現過)。  
光是這點就很難處理，在 n = 400 的限制下，共有 2^n 種不同的狀態，不太能夠接受。

---

實際上，我們並不在乎**填了什麼數**，只在乎**填了幾個數**、當前有**多少逆序對**。  

在我們填完 nums[i] 的數的當下，數列長度為 i + 1，且 i 的左方有 i 個數。  
最佳的情況下，左方 i 個數都比 nums[i] 還大，最多增加 i 個逆序對；最壞情況下，左方每個數都比 nums[i] 更小，增加 0 個逆序對。  

定義 dp(i, cnt)：在填完 perms[0..i] 時擁有 cnt 個逆序對，共有幾種填法。  
轉移：dp(i, cnt) = sum(dp(i - 1, cnt - x)) FOR ALL 0 <= x <= min(i, cnt)  
base：當 cnt 為負數，不合法，回傳 0；或限制存在時、且不滿足限制，也回傳 0；  
在 i = 0 時，若 cnt 也為 0，回傳 1，否則 0。  

時間複雜度 O(n \* M \* min(n, M))，其中 M = max(cnti)。  
空間複雜度 O(n \* M)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        limit = {}
        for i, cnt in requirements:
            limit[i] = cnt
            
        @cache
        def dp(i, cnt):
            if i == 0:
                return int(cnt == 0)
            if i in limit and limit[i] != cnt:
                return 0
            res = 0
            for j in range(min(i, cnt) + 1):
                res += dp(i - 1, cnt - j)
            return res % MOD
        
        return dp(n - 1, limit[n - 1])
```
