---
layout      : single
title       : LeetCode 2869. Minimum Operations to Collect Elements
tags        : LeetCode Easy Array HashTable
---
雙周賽114。

## 題目

輸入正整數陣列nums，還有整數k。  

每次操作，你可以移除nums的最後一個元素，並將其加入你的收藏。  

你想要收藏1\~k中的所有整數，求**最少**需要幾次操作。  

## 解法

只能移除最後一個元素，意味著需要倒序遍歷nums。  

我們只要找1~\k的元素，遍歷到的數字x若不超過k，則加入集合中，等集合裝滿k個元素則回傳答案。  

時間複雜度O(N)。  
空間複雜度O(k)。  

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=set()
        
        for i,x in enumerate(reversed(nums)):
            if x<=k:
                s.add(x)
            if len(s)==k:
                return i+1
```
