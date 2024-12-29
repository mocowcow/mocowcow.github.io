---
layout      : single
title       : LeetCode 3403. Find the Lexicographically Largest String From the Box I
tags        : LeetCode Medium Greedy
---
weekly contest 430。  
這題測資也很迷惑，我現在真的不懂垃扣對 N^2 答案的測資允許範圍是多少。  

## 題目

輸入字串 word 還有整數 numFriends。  

Alice 在和 numFriends 個朋友玩。  
遊戲會進行若干回合，每回合會：  

- 將 word 分割成 numFriends 個非空字串，且此分割方案與之前回合都**不相同**。  
- 將分割出的非空字串放入箱子中。  

在遊戲結束後，找到箱子中**字典序最大**的字串。  

## 解法

numFriends = 1 是最特殊的情況，不需分割，直接回傳 word。  

---

在一個字串後面追加字元，越加會使字典序越大。  
把字串成 numFriends 塊，為了使字典序越大，應**貪心**地使字串越長越好。

numFriends - 1 個人都只拿長度 1 的子字串，剩下一人可拿 sz =  N - nnumFriends + 1。  
枚舉所有長度為 sz 的子字串，找最大者。  

---

但是有可能答案長度並不一定是 sz，例如：  
> word = "aaz", numFriends = 2  
> sz = 3-2+1 = 2  
> 大小 2 的子字串只有 "aa", "az"  

但最大字典序是 "z"。  
因此還是需要枚舉每個 i 作為字串開頭。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
            
        N = len(word)
        sz = N - numFriends + 1

        return max(word[i:i+sz] for i in range(N))
```
