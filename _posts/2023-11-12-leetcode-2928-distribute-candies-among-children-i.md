---
layout      : single
title       : LeetCode 2928. Distribute Candies Among Children I
tags        : LeetCode Easy Simulation Math
---
雙周賽117。最近周賽真的是越來越扯，前兩題分別是分糖果1和2。但是在開賽的前幾日，分糖果3竟然以**付費題**的形式出現。  
而且內容完全一樣，只是測資範圍變大，直接向下兼容本次兩題。真的是pay to win。  

## 題目

輸入兩個正整數n和limit。  

把n個糖果分給3個小孩，且每個小孩最多拿limit個糖果。求有多少分法。  

## 解法

首先是暴力法，枚舉三個小孩的糖果數，剛好對上總數n就合法。  

時間複雜度O(limit^3)。  
空間複雜度O(1)。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans=0
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    if i+j+k==n:
                        ans+=1
                        
        return ans
```
