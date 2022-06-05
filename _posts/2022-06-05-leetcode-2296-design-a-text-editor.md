--- 
layout      : single
title       : LeetCode 2296. Design a Text Editor
tags        : LeetCode Hard String Design
---
周賽296。有點尷尬的題目，難度不高，但我選錯資料結構差點陣亡，好在剩下最後2分鐘趕快改過來。  

# 題目
設計一個有游標的文字編輯器，可以執行以下操作：  
- 將文字加到游標的位置  
- 刪除游標左方的文字(backspace鍵功能)  
- 左右移動游標  

刪除文字時，只會刪除游標左方的字元，而且永遠符合 0<=游標位置<=文字字元數。  

實作類別TextEditor：  
- 無參數建構子：以空白文字初始化  
- void addText(string text)：將text加入到當前游標位置，結束時游標應在text的右方  
- int deleteText(int k) 刪除游標左側最多k個字元，並回傳實際刪除的字元數  
- string cursorLeft(int k) 將游標向左移動k次，並回傳游標左側最多10個字元  
- string cursorRight(int k) 將游標向右移動k次，並回傳游標左側最多10個字元  

# 解法
看到需要頻繁左右移動和增減，馬上就想到要用linked list。  
結果我選了list沒錯，但python的list每次修改不是O(1)，最後還是要轉回字串，反而比用單純的字串效率更差。  
好在最後改回字串，總算是拿到AC。  

建構子：初始化空字串，以及游標位置0  
addText：以游標為中心將原字串切成兩半，中間塞入text，並將游標右移  
deleteText：先計算左方刪除k次後的游標位置，然後原字串連接，並將游標左移  
cursorLeft/cursorRight：先計算游標移動後的位置，然後從該位置往左取最多10個字元  

```python
class TextEditor:

    def __init__(self):
        self.text=''
        self.cs=0

    def addText(self, text: str) -> None:
        L,R=self.text[:self.cs],self.text[self.cs:]
        self.text=L+text+R
        self.cs+=len(text)

    def deleteText(self, k: int) -> int:
        if self.cs==0:
            return 0
        size=min(self.cs,k)
        self.text=self.text[:self.cs-size]+self.text[self.cs:]
        self.cs-=size
        return size

    def cursorLeft(self, k: int) -> str:
        self.cs=max(0,self.cs-k)
        return self.text[max(0,self.cs-10):self.cs]

    def cursorRight(self, k: int) -> str:
        self.cs=min(len(self.text),self.cs+k)
        return self.text[max(0,self.cs-10):self.cs]
```
