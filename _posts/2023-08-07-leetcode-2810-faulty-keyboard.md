---
layout      : single
title       : LeetCode 2810. Faulty Keyboard
tags        : LeetCode Easy Array String
---
周賽357。

## 題目

你的鍵盤有點故障，每次你按下按鍵"i"時，他會把已經輸入的字串反轉。其他按鍵都正常運作。  

輸入字串s，你必須按照s的順序在故障鍵盤按下相應的按鍵。  

求得到的字串結果。  

## 解法

按照題意模擬，只要碰到i就把字串翻轉，否則將字元加入字串尾端。  

因為字串串接每次複雜度是O(N)，所以先用list保存字元，最後處理完才轉換成字串。  

最差情況下，s的前半段都是非i字元，後半段全都是i，這樣會將長度N/2的字串翻轉N/2次。  
時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def finalString(self, s: str) -> str:
        st=[]
        for c in s:
            if c=="i":
                st=st[::-1]
            else:
                st.append(c)
                
        return "".join(st)
```
