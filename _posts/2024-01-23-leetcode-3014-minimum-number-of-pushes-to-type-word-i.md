---
layout      : single
title       : LeetCode 3014. Minimum Number of Pushes to Type Word I
tags        : LeetCode Easy String HashTable Greedy
---
周賽381。

## 題目

輸入由**不同**字元組成的字串 word。  
(進階版：有**重複**字元)

電話的每個按鍵可以對應到**不同**的字元集合，透過按下按鍵的次數來代表這些字元。  
例如：按鍵 2 對應到字元集合 ["a","b","c"]，如果按一次會得到 "a"，按兩次得到 "b"，按三次得到 "c"。  

你可以將按鍵 2\~9 重新對應到**不同**的字元集合。  
一個按鍵可以對應多個字元，但是一個字元只能對應到一個按鍵。  
你必須找到一種分配方式，其能夠使得拼出字串 word 所需的按鍵次數**最小化**。  

求拼出字串 word 所需要的**最少**按鍵次數。  

## 解法

2\~9 總共只有 8 個按鍵，代表有 8 個字母可以對應到 1 次按鍵。  
接下來的 8 個字母可以對應到 2 次按鍵，以次類推。  

初始按鍵次數為 1，每分配 8 個之後，按鍵次數上升 1。  
只要從最小的按鍵次數開始分配給每個字母即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        cost = 1
        cnt = len(word)
        
        while cnt > 0:
            ans += cost * min(cnt, 8)
            cost += 1
            cnt -= 8
            
        return ans
```

如果有重複按鍵，為了使總按鍵次數較小，優先把**出現次數的較多的**字元對應到**按鍵次數較少**的位置上。  

先統計各字元出現次數，並依照出現次數遞減排序。  
一樣從按鍵次數 1 開始分配，每分配 8 次，按鍵次數上升 1。  

雖然有排序，但其實最多只有 26 個字元，可以當作常數。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        ks = sorted(d.keys(), reverse=True, key=lambda x:d[x])
        q = deque(ks)
        
        cost = 1
        ans = 0
        while q:
            for _ in range(min(len(q), 8)):
                x = q.popleft()
                ans += d[x] * cost
            cost += 1
        
        return ans
```
