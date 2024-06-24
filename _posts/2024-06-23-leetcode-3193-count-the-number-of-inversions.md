---
layout      : single
title       : LeetCode 3193. Count the Number of Inversions
tags        : LeetCode Hard Array DP PrefixSum
---
雙周賽 133。根據經驗來講，這題應該頂多 500 人過。結果有 1800 人過了，不愧是雙周賽，非常魔幻。  

## 題目

輸入整數 n 和二維整數陣列 requirements，其中 requirements[i] = [end<sub>i</sub>, cnt<sub>i</sub>]，代表以前綴的最後一個索引，以及其**逆序對**的數量。  

一個索引數對 (i, j) 若滿足以下條件，則稱為**逆序對**：  

- i < j 且 nums[i] > nums[j]  

求數列 [0, 1, 2, ..., n - 1] 的排列中，有多少種排列**滿足所有**requirements[i]，也就是 perm[0..end<sub>i</sub>] 正好擁有 cnt<sub>i</sub> 個**逆順對**。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

題目是求**前綴**的逆序對數量，因此考慮在已有的數列 perm 末端加入新的數會有什麼影響。  
假設 perm = [2,0]，在末端加上 1 之後，產生了一個逆序對 (nums[0] = 2, nums[2] = 1)。  
每加入一個數 x 後，產生的逆序對數量等於左方大於 x 的數個數。  

為了計算增加的逆序對，需要維護左方有哪些數出現過 (同時也知道那些還沒出現過)。  
光是這點就很難處理，在 n = 400 的限制下，共有 2^n 種不同的狀態，不太能夠接受。

---

實際上，我們並不在乎**填了什麼數**，只在乎**填了幾個數**、當前有**多少逆序對**。  

nums 是 1 ~ n 的**排列**，每個數只出現一次。透過這個特性可以推斷出剩餘數字和當前數字的大小關係。  
試想有 [1,2,3,4] 共 n = 4 個數，現在要考慮最後一格填什麼：  

- [#,#,#,1] 填 1，剩下的 [2,3,4] 比 1 大，逆序對增加 3 個  
- [#,#,#,2] 填 2，剩下的 [3,4] 比 2 大，逆序對增加 2 個  
- [#,#,#,3] 填 3，剩下的 [4] 比 3 大，逆序對增加 1 個  
- [#,#,#,4] 填 4，剩下的全都比 4 小，逆序對不增加  

只要選擇 n 個數字最小的，就會得到 n - 1 個逆序對；選擇第 x 小的，就會得到 n - x 個逆序對。  
每次選擇，最增加至多 n - 1、至少 0 個逆序對。  

---

而且不管怎樣選，剩下的數字依然具有保留此特性，會縮減成**規模更小的子問題**。  
例如，求 n 個數湊出 cnt 個逆序對：  

- 選了第 1 小的數，得到 n - 1 個逆序對。  
    剩下 n - 1 個數，還要湊出 cnt - (n - 1) 個逆序對。  
- ...  
- 選了第 n 小的數，得到 n - n 個逆序對。  
    剩下 n - 1 個數，還要湊出 cnt - (n - n) 個逆序對。  

就範例 1 來看，原本是 [0,1,2] 三個數要湊出 2 個逆序對。  

- 填入 [#,0,1] 後，剩下 1 個數字，且還需要 1 個逆序對；
- 填入 [#,2,0] 後，剩下 1 個數字，且還需要 1 個逆序對。  

至於剩下的數字是什麼根本無所謂，反正我們只需要知道相對的大小關係。  
出現**重疊的子問題**，因此考慮 dp。  

---

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

仔細觀察 dp(i, cnt) 的轉移來源有那些？  
> dp(i - 1, cnt), dp(i - 1, cnt - 1) .., dp(i - 1, cnt - (i - 1)), dp(i - 1, cnt - i)  

那 dp(i, cnt - 1) 的轉移來源又有誰？  
> dp(i - 1, cnt - 1), dp(i - 1, cnt - 1 - 1) .., dp(i - 1, cnt - 1 - i)  

發現 dp(i, cnt) 比起 dp(i, cnt - 1) 來說，多出一個轉移來源 dp(i - 1, cnt)。  
並且在 cnt 比 i 還大時，會失去 dp(i - 1, cnt - 1 - i) 這個來源。  

總而言之，dp(i, cnt) 的轉移來源是所有 dp(i - 1, j) 的總和，其中 cnt - min(cnt, i) <= j <= cnt。  
這些重複的部分可以使用**滑動窗口**或是**前綴和**進行優化，每個狀態只需要 O(1) 時間轉移。  

時間複雜度 O(n \* M)，其中 M = max(cnti)。  
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
            if i < 0:
                return int(cnt == 0)
            if i in limit and limit[i] != cnt:
                return 0
            res = ps(i - 1, cnt)
            j = cnt - min(i, cnt)
            if j > 0:
                res -= ps(i - 1, j - 1)
            return res % MOD
        
        @cache
        def ps(i, cnt):
            if cnt < 0:
                return 0
            res = dp(i, cnt) + ps(i, cnt - 1)
            return res % MOD
        
        return dp(n - 1, limit[n - 1])
```
