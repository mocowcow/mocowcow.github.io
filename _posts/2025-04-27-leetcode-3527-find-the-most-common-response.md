---
layout      : single
title       : LeetCode 3527. Find the Most Common Response
tags        : LeetCode Medium Simulation
---
biweekly contest 155。  
怎麼感覺以後 Q1 都會是中等題了。  

## 題目

<https://leetcode.com/problems/find-the-most-common-response/>

## 解法

按照題意模擬，把每次回應去重後統計次數。  

時間複雜度 O(L)，其中 L = 字串總長度。  
空間複雜度 O(L)。  

```python
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        d = Counter()
        for a in responses:
            s = set(a)
            for x in s:
                d[x] += 1

        mx = 0
        ans = ""
        for k, v in d.items():
            if v > mx:
                mx = v
                ans = k
            elif v == mx and k < ans:
                ans = k

        return ans
```
