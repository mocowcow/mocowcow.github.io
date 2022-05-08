--- 
layout      : single
title       : LeetCode 2264. Largest 3-Same-Digit Number in String
tags        : LeetCode Easy String
---
周賽292。網站好像是被DDOS，周賽一開始就整個卡死，過了15分鐘才看到題目，後續還是間間段段的卡，答案都送不出去。

# 題目
輸入字串num。在nums中找到**最大**且由三個同樣數字組成的子字串，若不存在則回傳空字串。  
例：  
> num = "6777133339"  
> ans = "777"  
> num = "2300019"  
> ans = "000"
> num = "42352338"  
> ans = ""

# 解法
一開始我沒想太複雜，直接把問題拆成兩個部分：  
1. 找到連續出現的數字n  
2. 若n大於最大值mx則更新答案  

轉型和字串切割不少次，效率是差了一些。

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        N = len(num)
        i = 0
        ans = ''
        mx = -1
        while i+2 < N:
            if num[i] == num[i+1] == num[i+2]:
                n = int(num[i:i+3])
                if n > mx:
                    mx = n
                    ans = num[i:i+3]
            i += 1
        return ans
```

後來想想，空字串""小於"0"，好像直接比對就行，不需要額外維護最大值mx，最後把答案*3回傳就好。

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=''
        for i in range(2,len(num)):
            if num[i-2]==num[i-1]==num[i]:
                ans=max(ans,num[i])
        
        return ans*3
```

看看別人怎麼做，結果有個更聰明的解法，笑死我，這人腦筋轉得很快。  
直接從在num裡面從'999'往下找到'000'，中途有找到就直接回傳；最後沒找到才回傳空字串。

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in reversed(range(10)):
            if str(i)*3 in num:
                return str(i)*3
        
        return ''
```