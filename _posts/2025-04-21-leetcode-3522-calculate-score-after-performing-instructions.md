---
layout      : single
title       : LeetCode 3522. Calculate Score After Performing Instructions
tags        : LeetCode Medium Simulation
---
weekly contest 446。  
久違的 Q1 中等題，但感覺不太值中等。  

## 題目

<https://leetcode.com/problems/calculate-score-after-performing-instructions/description/>

## 解法

按照題意模擬即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        N = len(values)

        vis = [False] * N
        i = 0
        ans = 0
        while 0 <= i < N and not vis[i]:
            vis[i] = True
            if instructions[i] == "add":
                ans += values[i]
                i += 1
            else:
                i += values[i]

        return ans
```
