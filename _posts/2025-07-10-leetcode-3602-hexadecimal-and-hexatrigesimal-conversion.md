---
layout      : single
title       : LeetCode 3602. Hexadecimal and Hexatrigesimal Conversion
tags        : LeetCode Easy Simulation Math
---
biweekly contest 160。  
不知道算不算簡單，有點尷尬的題。  

## 題目

<https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/description/>

## 解法

按照題意模擬。  

沒寫過進制轉換可以從 [504. Base 7](https://leetcode.com/problems/base-7/) 改一下就行。  
好險我有準備模板。  

時間複雜度 O(log n)。  
空間複雜度 O()。  

```python

class Solution:
    def concatHex36(self, n: int) -> str:
        return convertToBase(n**2, 16) + convertToBase(n**3, 36)


# converse x to b-base
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convertToBase(x: int, b: int):
    if x == 0:
        return "0"
    sign = "" if x >= 0 else "-"
    x = abs(x)
    res = []
    while x > 0:
        r = x % b
        res.append(CHARS[r])
        x //= b
    res.reverse()
    return sign + "".join(res)
```
