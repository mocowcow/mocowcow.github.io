--- 
layout      : single
title       : LeetCode 2559. Count Vowel Strings in Ranges
tags        : LeetCode Medium Array String PrefixSum
---
周賽331。

# 題目
輸入整字串陣列words，以及二維整數陣列qeuries。  

其中queries[i] = [l<sub>i</sub>, r<sub>i</sub>]，代表你要查詢從words的第l<sub>i</sub>到第r<sub>i</sub>(兩者皆是**閉區間**)中，有幾個單字的字首和字尾皆為母音。  

回傳和qeuries同樣大小的陣列ans，其中ans[i]為第i次查詢的答案。  

注意：母音為為字母'a', 'e', 'i', 'o'和'u'。  

# 解法
先判斷各單字是否**首尾母音**，若是則該位置差分為1，做前綴和則可以O(1)查詢。  
然後遍歷一次查詢，從前綴和中計算求出區間和。  

時間複雜度O(N)。空間複雜度O(N)。  

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N=len(words)
        ps=[0]*(N+1)
        vowel=set("aeiou")
        
        for i in range(N):
            w=words[i]
            ps[i+1]=ps[i]+(w[0] in vowel and w[-1] in vowel)
            
        ans=[]
        for a,b in queries:
            x=ps[b+1]-ps[a]
            ans.append(x)
        
        return ans
```

同樣邏輯可以寫得更簡潔，複雜度不變。  

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ps=[0]
        for w in words:
            ps.append(ps[-1]+(w[0] in "aeiou" and w[-1] in "aeiou"))
        
        return [ps[b+1]-ps[a] for a,b in queries]
```