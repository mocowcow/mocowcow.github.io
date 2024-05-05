---
layout      : single
title       : LeetCode 3136. Valid Word
tags        : LeetCode Easy String Simulation
---
周賽 396。狗屎爛題，大概有一半的人都看不懂題意。而且還有小陷阱，差點吐血。  

## 題目

一個**合法**單字滿足：  

- 至少 3 個字元  
- 不可有數字、大小寫英文字母**以外**的字元  
- 至少一個母音  
- 至少一個子音  

輸入單字 word。  
若合法則回傳 true，否則回傳 false。

## 解法

其實不合法的字元就只有 @, #, $ 三種而已，確保這三個沒出現。  

另外要注意子音的部分。  
可能很多人想說**母音以外就是子音**，所以就寫了個判斷母音的反邏輯，獎勵你一個 WA。  
因為數字既非母音，也非子音。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def isValid(self, word: str) -> bool:
        
        def check1():
            return len(word) >= 3
        
        def check2():
            return all(c not in word for c in "@#$")
        
        def check3():
            return any(c in "aeiouAEIOU" for c in word)
        
        def check4():
            return any(c.isalpha() and c not in "aeiouAEIOU" for c in word)

        return check1() and check2() and check3() and check4()
```
