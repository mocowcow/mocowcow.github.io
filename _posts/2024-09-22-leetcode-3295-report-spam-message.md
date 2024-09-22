---
layout      : single
title       : LeetCode 3295. Report Spam Message
tags        : LeetCode Medium Simulation HashTable
---
weekly contest 416。  
印象中第一次出現中等的 Q1，但根本不如普通的簡單題。  

## 題目

輸入字串陣列 message 還有 bannedWords  

如果 message 中有**至少兩個**單字在 bannedWords 中出現，則視作**垃圾訊息**。  

若 message 是**垃圾訊息**回傳 true；否則回傳 false。  

## 解法

仔細看一下測資，bannedWords 長度高達 10^5，一定要用**集合**做。這可能是中等的原因。  
把 bannedWords 轉成集合，再算 message 中有幾個禁止字，根據數量回傳答案。  

時間複雜度 O(M + N)，其中 M = len(message)，N = len(bannedWords)。  
空間複雜度 O(N)。  

```python
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s = set(bannedWords)
        return len(1 for x in message if x in s) >= 2
```
