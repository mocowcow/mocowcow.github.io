---
layout      : single
title       : LeetCode 2810. Faulty Keyboard
tags        : LeetCode Easy Array String Simulation
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

可以使用雙向隊列，直接改變加入字元的方向來模擬翻轉。  

維護變數rev代表是否翻轉，若是則從左方加入字元，否則從右方加入。  
最後組合字串時，記得檢查是否翻轉過。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def finalString(self, s: str) -> str:
        q=deque()
        rev=False
        
        for c in s:
            if c=="i":
                rev=not rev
            elif rev:
                q.appendleft(c)
            else:
                q.append(c)
                
        ans="".join(q)
        if rev:
            return ans[::-1]
        else:
            return ans
```
