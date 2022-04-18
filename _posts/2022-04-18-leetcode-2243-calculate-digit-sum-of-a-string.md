---
layout      : single
title       : LeetCode 2243. Calculate Digit Sum of a String
tags 		: LeetCode Easy String
---
周賽289。稍微有點卡到的簡單題，差點沒看懂題目。

# 題目
輸入由數字組成的字串s，以及整數k。  
如果s長度大於k，則執行以下操作：  
1. 將字串分割為長度為k的子字串，最後一個子字串長度可能不滿足k  
2. 將每個子字串裡面的數字加總，如"346"為3+4+6=13，故變成"13"  
3. 將所有加總過的子字串合併，若長度依然超過k，則回到步驟1

# 解法
剛好python字串切割可以不必考慮長度不足的問題，comprehension又可以很快的完成字串轉數字陣列。  
每次切出長度k的子字串，把子字串每個字元x轉為整數後加總，再轉回字串，串接起來，重複到長度夠短為止。

```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            t=''
            for i in range(0,len(s),k):
                seq=s[i:i+k]
                t+=str(sum(int(x) for x in seq))
            s=t
        
        return s
```

如果在別的語言，切割子字串時需要使用min防止出界。

```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            t=''
            for i in range(0,len(s),k):
                seq=0
                for j in range(i,min(i+k,len(s))):
                    seq+=int(s[j])
                t+=str(seq)
            s=t
            
        return s
```