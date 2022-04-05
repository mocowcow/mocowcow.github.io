---
layout      : single
title       : LeetCode 2222. Number of Ways to Select Buildings
tags 		: LeetCode Medium DP Array
---
雙周賽75。一開始朝著top down方式想，差點做不出來，好險後來用手算出bottom up。

# 題目
輸入只由0和1組成的字串s，0代表辦公大樓，1代表餐廳。  
你要選擇隨機3棟建物抽查，但是為了公平起見，不能連續抽查同類型的建物。求有幾種抽查的方式。

# 解法
抽查第三棟房屋的方式是由抽查第二棟的方式生成，而抽查第二棟的方式由抽查第一棟生成。  
定義dp0, dp1, dp01, dp10，就像名稱一樣，對應抽查方式，抽查第三棟就直接加到ans去就好。  
遍歷每個字元c，如果c=0，就增加dp0, dp10, dp010的量；否則增加dp1, dp01, d0101的量。  

```python
class Solution:
    def numberOfWays(self, s: str) -> int:
        dp0=dp1=dp01=dp10=0
        ans=0
        for c in s:
            if c=='0':
                dp0+=1
                dp10+=dp1
                ans+=dp01
            else:
                dp1+=1
                dp01+=dp0
                ans+=dp10
            
        return ans
```

