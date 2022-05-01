--- 
layout      : single
title       : LeetCode 2260. Minimum Consecutive Cards to Pick Up
tags        : LeetCode Medium Array HashTable
---
周賽291。很棒的題目，非常適合初學者練習雜湊表。

# 題目
輸入整數陣列cards，代表不同卡片的數值，兩張同值的卡片可以成功配對。  
若配對第i和j張卡，你必須撿起i..j之間的所有卡片。求配對任意數值時，最少需要撿起幾張卡片。無法配對則回傳-1。  

例：  
> cards = [3,4,2,3]  
> 配對兩張3，要撿起[3,4,2,3]共四張

# 解法
先以卡片值分類，將索引加入雜湊表中，分別對每個卡片值的相鄰索引計算距離。

```python
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d=defaultdict(list)
        for i,n in enumerate(cards):
            d[n].append(i)
            
        ans=math.inf
        for v in d.values():
            for i in range(1,len(v)):
                ans=min(ans,v[i]-v[i-1]+1)

        if ans==math.inf:
            return -1
        return ans
```

其實不必保存所有索引，只要記錄上一次碰到的位置就可以。  

```python
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last={}
        ans=math.inf
        for i,c in enumerate(cards):
            if c in last:
                ans=min(ans,i-last[c]+1)
            last[c]=i
            
        return -1 if ans==math.inf else ans
```