--- 
layout      : single
title       : LeetCode 2580. Count Ways to Group Overlapping Ranges
tags        : LeetCode Medium Array Sorting Greedy
---
雙周賽99。

# 題目
輸入二維整數陣列ranges，其中ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]，代表start<sub>i</sub>到end<sub>i</sub>之間(都包含)都包含在第i個區間中。  

你要將所有區間分成**兩組**(可以為空)，滿足：  
- 每個區間只屬於其中一組  
- 任意兩個**有交集**的區間必須分到**同一組**  

若兩個區間包含**至少一個**公共整數，則為**有交集**的。  
- 例如[1,3]和[2,5]有公共整數2和3，所以有交集  

求有多少**分組方式**。答案很大，先模10^9+7後回傳。  

# 解法
先把所有交集的區間合併，看最後變成x個無交集區間。  
每個無交集區間可以分到第一組或第二組，則答案為2^x。  

如何合併區間？  
先將區間以起點排序後，遍歷每個區間[a,b]，如果a被先前區間的最末端end所包含，則有交集，視b的大小更新end；否則無交集，得到一個新的無交集區間，則計數cnt加一。  

最後回傳2的cnt次方。  

時間複雜度瓶頸在於排序的O(N log N)。空間複雜度O(1)。  

```python
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD=10**9+7
        cnt=0
        ranges.sort()
        
        end=-1
        for a,b in ranges:
            if end>=a:
                end=max(end,b)
            else:
                cnt+=1
                end=b
            
        return pow(2,cnt,MOD)
```

其實也可以邊合併區間，邊計算答案。  

```python
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD=10**9+7
        ranges.sort()
        
        end=-1
        ans=1
        for a,b in ranges:
            if a>end:
                ans=(ans*2)%MOD
            end=max(end,b)
            
        return ans
```