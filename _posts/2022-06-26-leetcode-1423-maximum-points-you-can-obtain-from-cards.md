--- 
layout      : single
title       : LeetCode 1423. Maximum Points You Can Obtain from Cards
tags        : LeetCode Medium Array SlidingWindow
---
每日題。有點像今早周賽Q3，如果今天有人先做完這題再去周賽，或許會更加順暢。  
昨晚打雙周賽，今早打周賽，打完更新win10，今天真是充實的一天。

# 題目
輸入整數陣列cardPoints，代表好幾張牌的點數，整數k代表可以選擇的牌數。  
你每次可以選擇排堆中最前或是最後一張牌，並獲得其分數。  
求最多可以獲得幾分。  

# 解法
只能從兩邊拿牌，不管怎樣拿，最後一定會剩下中心的一塊連續區域。  
與其列舉左右得到多少分，不如算出中間的N-k張牌的最小值為多少，剩餘的牌點數越小，則得分越大。  

若選擇牌數k和總牌數相等，可直接回傳cardPoints總和sm。  
列舉每個索引r為滑動窗口的右邊界，若大小滿足k，則以視窗內分數更新最小值mn。  
最後sm扣掉mn即是左右選牌可獲得的最大分數。  

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N=len(cardPoints)
        if k==N:
            return sum(cardPoints)
        
        size=N-k
        window=0
        mn=inf
        l=0
        for r in range(N):
            window+=cardPoints[r]
            if r-l+1==size:
                mn=min(mn,window)
                window-=cardPoints[l]
                l+=1

        return sum(cardPoints)-mn
```
