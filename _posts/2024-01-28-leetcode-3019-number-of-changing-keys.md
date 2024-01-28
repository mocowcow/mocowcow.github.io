---
layout      : single
title       : LeetCode 3019. Number of Changing Keys
tags        : LeetCode Easy String Simulation
---
周賽382。第一次看到只有 2 分的題目。  

## 題目

輸入字串 s，代表使用者的輸入。  
若使用者在輸入字串的時候需要按的按鍵和上次不同，則稱做**改按鍵**。  
例如：輸入 s = "ab" 需要改按鍵一次，而 s = "bBBb" 不需要改按鍵。  

求使用者需要改按鍵幾次。  

注意：使用 shift 或是 caps lock 這種輔助鍵**不算**是改按鍵。也就是說，連續輸入同一個字母的大小寫不用改按鍵。  

## 解法

不分大小寫，方便起見先把 s 統一轉成小寫。  

直接遍歷 s 中每個字母 c，若 c 與上一個字元不同則答案加 1。  

時間複雜度 O(n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        for a, b in pairwise(s.lower()):
            if a != b:
                ans += 1
                
        return ans
```

python 可以寫成一行簡潔版。  

```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(a != b for a, b in pairwise(s.lower()))
```
