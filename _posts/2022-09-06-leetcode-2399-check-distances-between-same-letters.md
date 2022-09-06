--- 
layout      : single
title       : LeetCode 2399. Check Distances Between Same Letters
tags        : LeetCode Easy Array String HashTable
---
周賽309。體會到zip函數有多好用，要不然整天對字元轉ascii後-97是真的有點麻煩。  

# 題目
輸入僅由小寫字母組成的字串s，其中s中的每個字母正好**出現兩次**。還有一個長度為26整數陣列distance。  
字母表中的每個字母都從0到25編號（即 'a' -> 0、'b' -> 1、'c' -> 2、...、'z' -> 25）。  

**間隔良好**的字串指的是：兩個同樣的字母之間包含的其他字母數正好為distance[i]。如果某個字母沒有出現在s中，那麼其對應的distance可以忽略。  

如果s是一個**間隔良好**的字串，則回傳true，否則回傳false。  

# 解法
本來還以為字母會出現多次，寫到一半才發現**有出現的話一定是兩次**。  

直接遍歷s中的每個字元c，以字母做分類裝進對應的雜湊表d中。  
依序檢查所有字母a\~z，若沒出現過就略過；否則檢查兩次出現位置中的間隔是否符合distance[i]。  

```python
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d=defaultdict(list)
        
        for i,c in enumerate(s):
            d[c].append(i)
            
        for c,dist in zip(string.ascii_lowercase,distance):
            if c not in d:continue
            if d[c][1]-d[c][0]-1!=dist:return False
            
        return True
```

不使用雜湊表，只用陣列紀錄索引位址也是可以，但是感覺比較醜。  
如果是第一次出現，則將索引寫入first；否則當前i和first中的索引檢查是否合法。  

```python
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first=[-1]*26
        
        for i,c in enumerate(s):
            x=ord(c)-97
            if first[x]==-1:
                first[x]=i
            else:
                if i-first[x]-1!=distance[x]:
                    return False 
                
        return True
```