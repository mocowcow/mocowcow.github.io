---
layout      : single
title       : LeetCode 3280. Convert Date to Binary
tags        : LeetCode Easy String
---
weekly contest 414。  

## 題目

輸入字串 date，代表公曆的日期格式 yyyy-mm-dd 格式。  

日期可以轉換為二進位表示的 year-month-day 格式，且沒有前導零。  

回傳 date 的二進位格式。  

## 解法

python 搞這題還真方便，內建 bin 函數就可以把整數轉成二進位字串。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ss = date.split("-")
        for i in range(3):
            x = int(ss[i])
            ss[i] = bin(x)[2:]

        return "-".join(ss)
```
