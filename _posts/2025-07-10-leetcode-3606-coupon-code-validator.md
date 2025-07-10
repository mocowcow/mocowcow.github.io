---
layout      : single
title       : LeetCode 3606. Coupon Code Validator
tags        : LeetCode Easy Simulation
---
weekly contest 457。  
滿臭長的 Q1。  
小抱怨一下參數名稱是單數，卡到我慣用變數名，有點不舒服。  

## 題目

<https://leetcode.com/problems/coupon-code-validator/description/>

## 解法

按照題意模擬即可。  

用雜湊表維護 code 的合法字元集。  
bussiness 也用雜湊表維護，順便映射到排序的順序大小。  
枚舉優惠券並篩選、最後排序。  

時間複雜度 O(L log N)，其中 L = 字串總長度。  
空間複雜度 O(L)。  

```python
BUSS_TYPE = {"electronics": 0, "grocery": 1,
             "pharmacy": 2, "restaurant": 3}
CODE_CHARS = set("_")
CODE_CHARS.update(string.ascii_letters)
CODE_CHARS.update(string.digits)


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        def code_ok(c):
            return c and all(x in CODE_CHARS for x in c)

        def buss_ok(b):
            return b in BUSS_TYPE

        ans = []
        for c, b, active in zip(code, businessLine, isActive):
            if code_ok(c) and buss_ok(b) and active:
                ans.append([BUSS_TYPE[b], c])
        ans.sort()

        return [c for _, c in ans]
```
