--- 
layout      : single
title       : LeetCode 2283. Check if Number Has Equal Digit Count and Digit Value
tags        : LeetCode Easy HashTable String
---
雙周賽79。腦子一下子沒轉過來，竟然卡住7分鐘才想通，原來是型別錯誤。

# 題目
輸入長度為n，索引從0開始的字串num，由數字組成。  
如果對所有的0<=i<n，所有的num[i]所對應的數字都剛好出現i次，則回傳true；否則回傳false。  

# 解法
要把num中每個數字字元都轉型成整數，然後用雜湊表計數。  
一開始我忘記轉型，想說怎麼答案都不對。  
然後再遍歷一次num，確認每個i和num[i]相同，否則回傳false。  

```python
class Solution:
    def digitCount(self, num: str) -> bool:
        num=[int(x) for x in num]
        ctr=Counter(num)
        for i,n in enumerate(num):
            if ctr[i]!=n:
                return False
            
        return True
```
