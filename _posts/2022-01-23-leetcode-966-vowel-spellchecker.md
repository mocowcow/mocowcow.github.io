---
layout      : single
title       : LeetCode 966. Vowel Spellchecker
tags 		: LeetCode Medium HashTable String
---
有點麻煩的題，比較注重題目理解及實作。

# 題目
以wordlist建立檢查方式：  
1. 完全符合，直接輸出
2. 大小寫不同，輸出預測的結果
3. 母音調換，輸出預測的結果
4. 皆不符合則輸出空字串

必須依照以上優先及順序匹配，且在有多種可能性時以**第一個結果**為準。

# 解法
對應各種條件：
1. 原字典直接裝進set
2. 一律將單字轉成小寫，放入dict
3. 將小寫字母音用'*'替代，放入dict
之後依序處理各查詢即可。

因為要求第一個符合的結果，所以建立映射的時候要額外檢查是否已經有存值，不得更新。

```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        VOWELS = set(list('aeiou'))
        exact = set(wordlist)
        cap = {}
        vow = {}

        def getPattern(x): return ''.join(['*' if c in VOWELS else c for c in x])

        for w in wordlist:
            lower = w.lower()  # cap
            ve = getPattern(lower)  # vowel errors
            if lower not in cap:
                cap[lower] = w
            if ve not in vow:
                vow[ve] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lower = q.lower()
            ve = getPattern(lower)
            if lower in cap:
                ans.append(cap[lower])
            elif ve in vow:
                ans.append(vow[ve])
            else:
                ans.append('')

        return ans
```
