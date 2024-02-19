---
layout      : single
title       : LeetCode 3042. Count Prefix and Suffix Pairs I
tags        : LeetCode Easy String
---
周賽385。最近字串題是真的很多，有好好補題的同學應該上了不少分。  

## 題目

輸入字串陣列 words。  

定義**布林**函數 isPrefixAndSuffix，接收兩個字串參數 str1 和 str2。  

- 若 str1 同時是 str2 的前綴及後綴，則回傳 true；否則回傳 false  

例如 isPrefixAndSuffix("aba", "ababa") 回傳 true，因為 "aba" 既是 "ababa" 的前綴，也是後綴；而 isPrefixAndSuffix("abc", "abcd") 回傳 false，因為 "abc" 不是 "abcd" 的後綴。  

求**有多少** isPrefixAndSuffix(words[i], words[j]) 為 true、且滿足 i < j 的數對 (i, j)。  

## 解法

在字串不多的時候，可以用暴力法。  
直接枚舉所有數對 (i, j)，斷 words[i] 是否為 words[j] 的前後綴。  

在判斷 s1 是否為 s2 的前綴時，直接取 s2 前方和 s1 長度相等的子字串，判斷是否等於 s1 即可；反之，後綴就取後方相等長度。  

時間複雜度 O(N^2 \* L)，其中 L = max(len(words[i]))。  
空間複雜度 O(L)，原地比較字串可達 O(1)。  

```python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, s1 in enumerate(words):
            size = len(words[i])
            for s2 in words[i+1:]:
                pref = s2[:size]
                suff = s2[-size:]
                if s1 == pref and s1 == suff:
                    ans += 1
                    
        return ans
```
