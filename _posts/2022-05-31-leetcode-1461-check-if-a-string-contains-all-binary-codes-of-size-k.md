--- 
layout      : single
title       : LeetCode 1461. Check If a String Contains All Binary Codes of Size K
tags        : LeetCode Medium String BitManipulation RollingHash
---
每日題。這幾天好像都是位元運算，滿有趣的題目，其實rolling hash跟sliding window有八成像。

# 題目
輸入二進位字串s整數k，如果每個長度為k的二進位字串都是s的子字串，則回傳true。否則回傳false。

# 解法
題目講得有點不太清楚，換個說法：  
長度為k的二進位的排列全部都要出現過一次，例如：  
> k=2 sub=[00,01,10,11]  
> k=3 sub=[000,001,010,011,100,,101,110,111]  

計算出會有2^k個排列。  

以mask來表示當前子字串，每讀入一個新的字元時，先將mask左移一格，並將出界位元清除，在和當前的位元做OR運算。例如：  
> s = "110110", k = 2  
> s[1]=1, 子字串=11,  mask=11  
> 讀入s[2]=0, mask向左移=110  
> mask清掉出界位元 mask=10  
> mask和當前位元做OR mask=10  

每次將mask加入集合中去重複，最後若集合大小等於2^k，則代表每種排列都出現過。

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N=len(s)
        seen=set()
        mask=0
        clear=(1<<k)
        for i in range(N):
            mask=(mask<<1)|(s[i]=='1')
            mask&=~clear
            if i+1>=k:
                seen.add(mask)

        return len(seen)==(2**k)
```
