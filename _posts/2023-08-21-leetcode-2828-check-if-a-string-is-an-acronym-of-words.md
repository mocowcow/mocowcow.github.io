---
layout      : single
title       : LeetCode 2828. Check if a String Is an Acronym of Words
tags        : LeetCode Easy String Simulation
---
周賽359。學到一個新的單字。Acronym指的是好幾個單字的字首縮寫，例如GLHF = Good Luck Have Fun。  

## 題目

輸入字串陣列words和字串s，判斷s是不是words的字首縮寫。  

例如["apple", "banana"]的字首縮寫是"ab"，而["bear", "aardvark"]的字首縮寫是"ba"。  

## 解法

大前提，縮寫的長度必需和單字數相同。  
按照題意逐一檢查字首即可。  

時間複雜度O(N)，其中N為s長度。  
空間複雜度O(1)。  

```python
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        
        for i,c in enumerate(s):
            if c!=words[i][0]:
                return False
        
        return True
```

python快樂一行版本，雖然需要額外空間。  

時間複雜度O(M+N)，其中N為s長度，M為words長度。  
空間複雜度O(M)。  

```python
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s=="".join(w[0] for w in words)
```

其實還有常數空間的版本。  

時間複雜度O(N)，其中N為s長度，M為words長度。  
空間複雜度O(1)。  

```python
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words)==len(s) and all(w[0]==s[i] for i,w in enumerate(words))
```
