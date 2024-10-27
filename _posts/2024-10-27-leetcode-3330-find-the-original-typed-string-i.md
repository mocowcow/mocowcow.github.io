---
layout      : single
title       : LeetCode 3330. Find the Original Typed String I
tags        : LeetCode Easy
---
biweekly contest 142。  
題目有點難懂，害我卡一下。  

## 題目

Alice 想在電腦上輸入某個字串。  
但他有時候會手殘，按著按鍵太久，讓一個字元輸入好幾次。  

雖然他很專心，但還是會**失誤至多一次**。  

輸入字串 word，代表 Alice 螢幕上顯示的**最終結果**。  

求 Alice 一開始原本想輸入的字串有幾種可能。  

## 解法

失誤是**按著不放**，會讓某個字元 c 連續出現。  
原本連續出現 cnt 次的字元 c，其實他可能是想按 [1, cnt] 次，加上 x 個多壓著多打的。  

把 s 分成若干段連續的字元，每段的長度是 cnt。  
但他**至多失誤一次**，也就是選擇其中一段失誤，每段有 cnt-1 種失誤方案。  

根據**加法原理**，答案就是每段失誤方案加總，再加上**無失誤**的方案 1 種。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        N = len(word)
        i = 0
        ans = 1
        while i < N:
            j = i
            while j+1 < N and word[i] == word[j+1]:
                j += 1
            # cnt = j - i + 1
            # ans += cnt-1
            ans += j - i
            i = j + 1

        return ans
```

內建的 groupby 就能把連續的元素分組，並回傳每組的 (key, generator)。  

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for _, group in groupby(word):
            ans += len(list(group)) - 1

        return ans
```
