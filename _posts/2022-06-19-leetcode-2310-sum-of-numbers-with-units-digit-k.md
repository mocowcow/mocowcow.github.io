--- 
layout      : single
title       : LeetCode 2310. Sum of Numbers With Units Digit K
tags        : LeetCode Medium Math
---
周賽298。超級多edge case的數學題，吃了一個WA兩個TLE才釐清所有狀況。  

# 題目
輸入兩個整數num和k，試找出符合以下規則的正整數集合：  
- 每個數的個位數字為k  
- 所有數的總和為num  

回傳此集合的最小大小，若不存在則回傳-1。  
註：集合可包含重複數字，且空集合的總和視為0。  

# 解法
既然例題三都說了空集合視為0，只少可以先確定num為0時答案一定是0。  

我想著每次增加k，答案也加1，直到個位數的數字和num相同為止，反正超過10的部分都可以分散在任意的數字中填補。結果來了個k=0，尾數永遠不變，造成死循環TLE。  
這下知道要特別處理k=0，如果num尾數也是0，那剛好可以用一個數字來達成，否則回傳-1。  

那繼續從k開始，每次遞增k，直到個位數相同。考慮以下例子：  
> num=10, k=8  
> 需要5個k才能使尾數變成0，但是總和已經是40了  

如果總和超過num，也代表不可能達成，回傳-1；否則回傳使用了多少個k。

```python
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0

        if k==0:
            if num%10==0:
                return 1
            return -1
        
        sm=k
        ans=1
        while num>sm and num%10 != sm%10:
            sm+=k
            ans+=1
            
        if sm>num:
            return -1

        return ans
```
