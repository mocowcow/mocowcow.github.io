--- 
layout      : single
title       : LeetCode 1048. Longest String Chain
tags        : LeetCode Medium String Array DP HashTable
---
每日題。之前寫過兩次，但是完全看不懂之前在寫什麼鬼，整個思路都不一樣了。

# 題目
輸入一個words陣列，其中每個單字都由小寫英文字母組成。  
若我們可以在wordA的某個位置插入新字元，使之成為wordB，則稱wordA是wordB的**前身**。  
例如，"abc"是"abac"的前身，而"cba"不是"bcad"的前身。  

**單字鍊**指的是一個單字序列[word1, word2, ..., wordk]，且k>=1，每個word皆為其後方word的**前身**。  
回傳從words中可以組成的**最長單字鍊**長度。  

# 解法
對於某個單字w長度為x，那麼他可以作為(x+1)*26種單字的前身，複雜度是稍微高了一些。  
提示說：與其在w上插入新的字元，不妨試著刪掉某個字元。這樣複雜度就是剩下O(x)了。    

那麼我們的問題簡化成words中所有單字中，可以往前找到多少前身，答案就是找到的前身數+1。  
定義dp(w)為：單字w可以組成的最大單字鍊長度。  
轉移方程式：dp(w) = 1 + max(dp(pred) FOR ALL pred in words)  
base cases：當w長度為1時，不會再有前身了，直接回傳1。  

但是最長的單字鍊不一定是從最長的word開始而成，所以要從所有單字出發，並找出最佳結果。  

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wd=set(words)
        
        @cache
        def dp(w):
            if len(w)==1:
                return 1
            best=0
            for i in range(len(w)):
                pred=w[:i]+w[i+1:]
                if pred in wd:
                    best=max(best,dp(pred))
            return best+1
   
        return max(dp(w) for w in words)
```
