--- 
layout      : single
title       : LeetCode 2315. Count Asterisks
tags        : LeetCode Easy String
---
雙周賽81。這題還滿有趣的，看了他人解法才發現我的比較不同，其實我的解法應該比較好想到才對，怎麼都沒人這樣做。

# 題目
輸入字串s，其中每兩個連續的'|'符號組成配成一對。例如第1和第2個'|'成一對、第3和第4個'|'成一對，以此類推。  
計算出有多少'*'符號不被'|'對所包住。  

# 解法
假設有n個'|'符號，那可以分割出n+1個子字串，而奇數索引的子字串都被'|'對包住，所以我們只要計算偶數索引的子字串中有多少個'*'號。  

```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        ss=s.split('|')
        ans=0
        for i in range(0,len(ss),2):
            ans+=ss[i].count('*')
        
        return ans
```

可是看到其他人的解法幾乎都是用這種，以變數ok表示當前範圍是否被'|'所包夾，只需要一次字串遍歷。  
ok初始值為true，每碰到新的'|'號，則將ok做not運算。只有在ok為真時，碰到'*'才把答案+1。  

```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        ans=0
        ok=True
        for c in s:
            if c=='|':
                ok=not ok
            elif c=='*' and ok:
                ans+=1
            
        return ans
```
