--- 
layout      : single
title       : LeetCode 2299. Strong Password Checker II
tags        : LeetCode Easy String
---
雙周賽80。超級手速題，真是好險有記住string函數庫，不然真的要手敲a\~z字母，敲到手痠。  

# 題目
一個密碼若滿足以下所有條件，則可稱為強密碼：  
- 至少8個字元  
- 至少有一個小寫字母  
- 至少有一個大寫字母  
- 至少有一個數字  
- 至少有一個特殊字元。特殊字元指的是"!@#$%^&*()-+"  
- 沒有連續出現相同的字元  

輸入字串password，判斷其是否為強密碼。  

# 解法
先檢查長度，不到8直接回傳False。  
維護變數up, low, digit, spec分別代表大寫、小寫、數字、特殊字元，而prev代表上一次出現的字元，用來檢查連續的相同字元。  
遍歷password中的字元c，檢查其所屬類型，並將對應的種類標記為1。順便檢查是否和prev相同，若是則直接回傳False。  
處理完字串後對四個種類做AND運算，判斷出是否為強密碼。  

```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        
        digit=spec=low=up=0
        prev=None
        for c in password:
            if c in string.ascii_lowercase:
                low=1
            elif c in string.ascii_uppercase:
                up=1
            elif c in string.digits:
                digit=1
            else:
                spec=1
            if c==prev:
                return False
            prev=c
        
        return low and up and spec and digit
```
