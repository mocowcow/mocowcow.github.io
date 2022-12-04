--- 
layout      : single
title       : LeetCode 2490. Circular Sentence
tags        : LeetCode Easy Array String
---
周賽322。沒有把題目看完，拿一個WA，有夠丟臉。  

# 題目
**句子**指的是由空格分隔的數個單字，且沒有前導、後導空白字元。  

單字只由英文字母組成，且大小寫視為不同。  

一個**環狀句子**需要符合：  
- 每個單字的最後一個字元，需要等於下一個單字的第一個字元  
- 最後一個單字的最後一個字元，需要等於第一個單字的第一個字元  

輸入字串sentance，判斷其是否為**循環句子**。  

# 解法
按照題目做，先把sentence以空白分割成數個字串，分別檢查第i個字串首字元是否等於i-1的尾字元。  
記得檢查**最後一個字串**以及**第一個字串**。  

python支援負數索引，在i=0時，索引-1可以存取到倒數第一個字串，所以不需要特別處理。  

時間瓶頸為split函數O(N)，空間取決於split之後的字串數量，最多可能有N/2個，視為O(N)。  

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ss=sentence.split(" ")
        N=len(ss)
        
        for i in range(N):
            a=ss[i-1]
            b=ss[i]
            if a[-1]!=b[0]:return False
            
        return True
```

原來大神的思維和普通的就是不同，其實根本不需要split。  
只要檢查**空白左右的字元**，還有**字串的首尾字元**是否相同即可。  

時間一樣是O(N)，但空間將低到O(1)。  

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        for i,c in enumerate(sentence):
            if c==" ":
                if sentence[i-1]!=sentence[i+1]:return False
        
        return sentence[0]==sentence[-1]
```