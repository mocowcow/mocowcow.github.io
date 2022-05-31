--- 
layout      : single
title       : LeetCode 2288. Apply Discount to Prices
tags        : LeetCode Medium String
---
周賽295。太久沒有搞字串格式化，還去查了一下怎麼用，好在是沒有BUG安全解決。

# 題目
sentence是由空白分隔的單字所組成的字串，其中每個單字可以包含數字、小寫字母和美元符號"$"。  
如果一個單字是一個非負實數，且前面有一個"$"，即是一個價格。  

例如："$100"、"$23"和"$6.75"代表價格，而"100"、"$"和"2$3"不代表價格。

輸入字串sentence，代表一個句子，還有一個整數discount。對所有價格進行discount%的折扣。所有價格都應該精確到小數點後兩位。  
回傳經過折扣修改後的sentence。  

# 解法
這題除了折扣完的小數點之外，判斷單字是否為**價格**也很麻煩。  
當時我只想到價格有幾個必要條件：  
1. 長度至少2  
2. 開頭為$  
3. 剩下的字元都是數字  

依照這三個順序做檢查，如果全部符合才將索引1開始的子字串進行折扣。

```python
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        NUM=set(list('0123456789'))
        
        def f(n):
            p=n/100*(100-discount)
            p="{:.2f}".format(p)
            return str(p)
        
        ss=sentence.split(' ')
        for i in range(len(ss)):
            s=ss[i]
            if s[0]!='$' or len(s)<2:
                continue
            ok=True
            for c in s[1:]:
                if c not in NUM:
                    ok=False
            if not ok:
                continue
            n=int(s[1:])
            price=f(n)
            ss[i]='$'+price
            
        return ' '.join(ss)
```

後來看其他python大老寫法，才發現原來可以使用isdigit方法來判斷字串是否全為數字。  

```python
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def convert(n):
            p=int(n)/100*(100-discount)
            return '$%.2f' % p
        
        ss=sentence.split()
        for i in range(len(ss)):
            if len(ss[i])>1 and ss[i][0]=='$':
                p=ss[i][1:]
                if p.isdigit():
                    ss[i]=convert(p)  
                
        return ' '.join(ss)
```

再多看看幾個榜上前幾名，發現不少人都用例外處理的方式來找價格。  
雖然說try很影響效能而且很醜，但這確實是比賽中最快速的方法。

```python
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def convert(n):
            p=int(n)/100*(100-discount)
            return '$%.2f' % p
        
        ss=sentence.split()
        for i in range(len(ss)):
            if len(ss[i])>1 and ss[i][0]=='$':
                try:
                    price=convert(ss[i][1:])
                    ss[i]=price
                except:
                    pass
                    
        return ' '.join(ss)
```