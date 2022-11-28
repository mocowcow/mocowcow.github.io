--- 
layout      : single
title       : LeetCode 2481. Minimum Cuts to Divide a Circle
tags        : LeetCode Easy Math
---
雙周賽92。聽說很多人都被egde case搞到，難得我有思慮周全，給自己一個鼓勵。  

# 題目
一個圓形的有效切割必須是：  
- 與邊上兩點及圓心形成的直線  
- 或 由邊上一點與圓心連成的直線  

輸入整數n，求最少需要幾次切割才能將圓分成n等分。  

# 解法
從最小的方案數開始往上窮舉，1等分不用切、2等分切1刀，這兩個都是n-1。  
再來看3等分要切3刀、4等分切2刀、5等5刀、6等3刀等，開始以此規律循環，得到規律：奇數需要n刀；偶數則需要n/2刀。  

```python
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n<2:return n-1
        if n%2==0:return n//2
        return n
```
