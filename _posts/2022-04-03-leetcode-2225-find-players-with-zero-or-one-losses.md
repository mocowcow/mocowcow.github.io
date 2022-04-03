---
layout      : single
title       : LeetCode 2225. Find Players With Zero or One Losses
tags 		: LeetCode Medium HashTable Array 
---
周賽287。不小心打錯噴一次WA。不知道為啥官方放了個graph標籤，明明完全沒相關。

# 題目
二維陣列matches代表比賽的勝負，matches[0]是贏家，而matches[1]是輸家。回傳長度為2的陣列ans，其中ans[0]為沒有輸過的選手，ans[1]為只輸過一次的選手。

# 解法
遍歷matches，把所有參賽者加入雜湊集players中，並以雜湊表lose計算每個人的敗場。  
遍歷players，如果敗場剛好為0或是1則加入對應的陣列中。

```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose=Counter()
        players=set()

        for a,b in matches:
            players.add(a)
            players.add(b)
            lose[b]+=1
            
        a0=[]
        a1=[]

        for p in players:
            if lose[p]==0:
                a0.append(p)
            elif lose[p]==1:
                a1.append(p)
                
        return (sorted(a0),sorted(a1))
```

