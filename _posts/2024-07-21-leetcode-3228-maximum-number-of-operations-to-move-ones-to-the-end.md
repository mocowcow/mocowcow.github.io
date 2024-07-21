---
layout      : single
title       : LeetCode 3228. Maximum Number of Operations to Move Ones to the End
tags        : LeetCode Medium Array Greedy
---
weekly contest 407。  

## 題目

輸入二進位字串 s。  

你可以執行以下操作任意次：  

- 選擇任意索引 i，滿足 i + 1 < s.length 且 s[i] == '1' 且 s[i + 1] == '0'。  
- 然後將 s[i] 右移到，直到他碰到另一個 "1" 或是抵達字串末端為止。  
    例如 s = "010010"，選擇 i = 1 操作後的結果是 s  = "000110"。  

求**最多**可以執行幾次操作。  

## 解法

舉個簡單例子：  
> s = 1010  
> 如果先移右邊的 1、再移左邊的 1，總共只能 2 次操作  
> 如果先移動左、再移右邊的，之後可以再移左邊的一次  

每次移動某個 1 時，會使得左方的 cnt 個 1 都可以再次移動。  
為使操作次數盡可能多，應從左至右逐批移動所有的 1。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxOperations(self, s: str) -> int:
        space = False
        ans = 0
        cnt1 = 0
        for c in s:
            if c == "0":
                space = True
            else:
                if space:
                    ans += cnt1
                    space = False
                cnt1 += 1

        if space:
            ans += cnt1

        return ans
```
