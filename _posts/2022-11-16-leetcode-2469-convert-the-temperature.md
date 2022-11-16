--- 
layout      : single
title       : LeetCode 2469. Convert the Temperature
tags        : LeetCode Easy Math
---
周賽319。這大概是哩扣全站最簡單的題目之一，竟然連浮點數精度誤差範圍都這麼寬。  

# 題目
輸入整數celsius代表攝氏溫度。  
將celsius轉換為克氏和華氏溫度，並回傳一個陣列ans = [克氏溫度, 華氏溫度]。  

注意：  
- 克氏 = 攝氏 + 273.15  
- 華氏 = 攝氏 * 1.80 + 32.00  

# 解法
浮點數加法和乘法不會造成精度誤差，直接將攝氏的值帶入公式就好。  

```python
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15,celsius*1.80+32.00]
```
