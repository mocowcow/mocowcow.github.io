--- 
layout      : single
title       : LeetCode 2284. Sender With Largest Word Count
tags        : LeetCode Medium Array String Sorting HashTable
---
雙周賽79。挺簡單的一題，但是我不小心記錯split用法，吃了一個WA。

# 題目
你有n條聊天訊息。輸入兩個字串陣列messages和senders，其中messages[i]是senders[i]發送的訊息。  
訊息由空白字元所分隔成多個單字，且不會有前導及尾隨空白。一個發件人可以發送多條訊息。    
回傳發送單字數最多的發件人。如果有多個發件人單字數相同​​，則回傳字典順序最大者。

# 解法
維護雜湊表ctr，用以紀錄各發件人的單字數。  
遍歷messages及senders，先把每個訊息以空白字元分割，求出總共有多少單字數，再加到對應的發件人計數上。  
最後篩選出所有單字數最多的發件人，並以遞減排序，回傳第一個就是答案。

```python
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        ctr=Counter()
        for msg,name in zip(messages,senders):
            ss=msg.split()
            ctr[name]+=len(ss)
            
        mx=max(ctr.values())
        cand=[k for k,v in ctr.items() if v==mx]
        return sorted(cand,reverse=True)[0]
```
