--- 
layout      : single
title       : LeetCode 2485. Find the Pivot Integer
tags        : LeetCode Easy Array PrefixSum
---
周賽321。

# 題目
輸入整數n，找到**中樞整數**x使得：  
- 1\~x的加總 和 x\~n的加總相等  

回傳**中樞整數**x，若不存在則回傳-1。題目保證至多只會有一個中樞。  

# 解法
話不多說，先來個暴力法，窮舉中樞點，計算並比對前後加總。  

時間O(N^2)，空間O(1)。  

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1,n+1):
            pref=sum(range(1,x+1))
            suff=sum(range(x,n+1))
            if pref==suff:return x
            
        return -1
```

左半邊都是呈現遞增，而右半邊遞減，可以用前綴和節省計算次數。  
對於每個中樞x來說，左半邊會比x-1為中樞時增加x，而右半邊會減少x-1。  

時間O(N)，空間O(1)。  

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        pref=0
        suff=n*(n+1)//2
        
        for x in range(1,n+1):
            pref+=x
            suff-=x-1
            if pref==suff:return x
            
        return -1
```

