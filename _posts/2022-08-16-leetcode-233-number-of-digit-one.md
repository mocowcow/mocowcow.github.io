--- 
layout      : single
title       : LeetCode 233. Number of Digit One
tags        : LeetCode Hard DP
---
數位DP練習題。

# 題目
輸入整數n，求所有小於等於n的正整數中總共出現多少個數字1。  

# 解法
這題除了位數受到n的的限制以外，沒有其他複雜的規定，數字0~9都可以任意選用。  
但是我們要計算出現過多少個1，所以需要一個變數cnt_one來計算到目前為止使用過幾個數字1，在所有位數處理完之後，才回傳cnt_one。  

例如：  
> n=13  
> 01提供一個1
> 10, 12, 13各提供一個1  
> 11提供兩個1  
> 共6個1

若當前第i個位數受到n限制，則上限up設為s[i]；否則0~9都可以使用。同樣的，若當前受限於n，又選擇了上限up作為該為數字，則下一個位數也會持續受到限制；否則下一位數可以任意選擇0~9而不會超過n。  
剩下只要列舉所有可用的數字j，若為1則使one_cnt計數+1，遞迴處理下一個位數。  

```python   
class Solution:
    def countDigitOne(self, n: int) -> int:
        s=str(n)
        N=len(s)
        
        @cache
        def dp(i,is_limit,cnt_one):
            if i==N:return cnt_one
            up=int(s[i]) if is_limit else 9
            ans=0
            for j in range(up+1):
                ans+=dp(i+1,is_limit and j==up,cnt_one+(j==1))
            return ans
               
        return dp(0,True,0)
```
