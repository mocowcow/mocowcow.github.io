--- 
layout      : single
title       : LeetCode 902. Numbers At Most N Given Digit Set
tags        : LeetCode Hard DP
---
數位DP練習題。

# 題目
輸入一個遞增排序的整數陣列digtis。你可以使用digit中的任意數字任意次，來組成新的整數。  
例如digits = ['1','3','5']，則可以組成'13','551','135315'等整數。

回傳可組成小於等於n的整數有多少。  

# 解法
這題相較之下簡單很多，符合n的限制以外，只要求使用的位數在digits陣列之中。  
而且digits陣列已經是遞增且不包含重複數字，我們只要依照當前位數是否受限於n來決定上限，列舉所有可使用的數字即可。  

```python
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s=str(n)
        N=len(s)
        digits=list(map(int,digits))
        
        @cache
        def dp(i,is_limit,is_num):
            if i==N:
                return is_num
            up=int(s[i]) if is_limit else 9
            ans=0
            if not is_num:
                ans=dp(i+1,False,False)
            for j in digits:
                if j>up:break
                ans+=dp(i+1,is_limit and j==up,True)
            return ans
        
        return dp(0,True,False)
```
