---
layout      : single
title       : LeetCode 1672. Richest Customer Wealth
tags 		: LeetCode Easy Matrix
---
今天除夕，新年快樂！

# 題目
輸入M*N的矩陣accounts，accounts[i][j]代表客戶i的第j個銀行帳號，求最有錢的客戶總共有多少財產。

# 解法
來個pythonic code，對accounts中每個元素代入sum，取最大值。

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(lambda x: sum(x), accounts))
```
