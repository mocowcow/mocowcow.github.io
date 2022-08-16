--- 
layout      : single
title       : LeetCode 1012. Numbers With Repeated Digits
tags        : LeetCode Hard DP Bitmask
---
[2376. count special integers]({% post_url 2022-08-15-leetcode-2376-count-special-integers %})的原題，程式碼幾乎一樣。  

# 題目
輸入一個整數n，回傳在[1, n]範圍內有多少正整數**至少出現一次重複數字**。  

# 解法
雖然已經知道是數位dp題型，但一開始想半天，還真沒想到怎麼判斷數字是否出現過。  

結果是找出不重複的整數扣掉，n個整數找到其中x個沒有重複的，得到n-x=m個有重複整數。  
使用數位dp，找到小於n，且每個數字只出現一次的整數，回傳n-dp就是答案。  

```python
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s=str(n)
        N=len(s)
        
        @cache
        def dp(i,mask,is_limit,is_num):
            if i==N:return is_num
            up=int(s[i]) if is_limit else 9
            down=0 if is_num else 1
            ans=0
            if not is_num:
                ans=dp(i+1,0,False,False)
            for j in range(down,up+1):
                if mask&(1<<j):continue
                new_mask=mask|(1<<j)
                new_limit=is_limit and j==up
                ans+=dp(i+1,new_mask,new_limit,True)
            return ans
            
        return n-dp(0,0,True,False)
```
