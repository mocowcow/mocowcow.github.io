---
layout      : single
title       : LeetCode 767. Reorganize String
tags        : LeetCode Medium Greedy Math
---


## 題目

<https://leetcode.com/problems/reorganize-string/>

## 解法

**鴿巢原理**經典題。

有 S 個格子，要求相鄰元素互相不同，則同一種元素至多可以放 ceil(S/2) 個。  

設元素個數最多的為 MX，若 MX 不超過 ceil(S/2) 則保證可以相鄰不同。  
依照元素個數遞減排序後，從最多的開始放。  
先放偶數格子，放完再放奇數格子。  

時間複雜度 O(N + D log D)，其中 D = 不同元素個數，本題為 26。  
空間複雜度 O(N + D)。  

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        pairs = cnt.most_common()  # 按照出現次數遞減排序

        S = len(s)  # 總個數
        MX = pairs[0][1]  # 最大出現次數

        # 最大的超過一半
        # if MX > (S + 1) // 2:
        if MX > (S - MX) + 1:
            return ""

        ans = [None] * S
        i = 0  # 先填偶數位
        for k, v in pairs:
            for _ in range(v):
                ans[i] = k
                i += 2
                if i >= S:  # 偶數填完，填奇數位
                    i = 1

        return "".join(ans)
````
