---
layout      : single
title       : LeetCode 3365. Rearrange K Substrings to Form Target String
tags        : LeetCode Medium HashTable Sorting
---
weekly contes 425。  
Q2 難度突然降低超多，而且竟然沒陷阱。  

## 題目

輸入兩個字串 s 和 t，兩者互為**易位構詞**。  
還有整數 k。  

你的目標是判斷是否能把 s 分割成 k 個相同大小的子字串，然後重排變成 t。  

若可能則回傳 true，否則回傳 false。  

## 解法

原本應該判斷 N 是否能被 k 整除，但是題目很良心，保證能整除。  

將 s, t 都切成 k 個子字串。  
既然能重排，只要兩者是由個數相同的子字串組成即可。  

可以使用雜湊表計數或將所有子字串排序後比對檢查。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        N = len(s)
        sz = N // k
        d1 = Counter()
        d2 = Counter()
        for i in range(0, N, sz):
            sub1 = s[i:i+sz]
            d1[sub1] += 1
            sub2 = t[i:i+sz]
            d2[sub2] += 1

        return d1 == d2
```

使用排序判斷。  

時間複雜度 O(N log k)。  
空間複雜度 O(N)。  

```python
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        N = len(s)
        sz = N // k
        a1 = []
        a2 = []
        for i in range(0, N, sz):
            sub1 = s[i:i+sz]
            a1.append(sub1)
            sub2 = t[i:i+sz]
            a2.append(sub2)

        return sorted(a1) == sorted(a2)
```
