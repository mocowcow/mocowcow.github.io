--- 
layout      : single
title       : LeetCode 2586. Count the Number of Vowel Strings in Range
tags        : LeetCode Easy String Array HashTable
---
模擬周賽336。去參加婚禮沒打這次周賽。  

# 題目
輸入字串陣列string以及兩個整數left和right。  

如果一個字串的第一個字元和最後一個字元都是母音，則稱為**母音字串**。  

求第left到第right個字串中，有幾個**母音字串**。  

# 解法
很單純的題目，只要遍歷指定範圍內的字串，檢查首尾是否為母音就行。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel=set("aeiou")
        ans=0
        
        for i in range(left,right+1):
            w=words[i]
            if w[0]in vowel and w[-1] in vowel:
                ans+=1
                
        return ans
```
