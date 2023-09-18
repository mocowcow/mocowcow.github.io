---
layout      : single
title       : LeetCode 2861. Maximum Number of Alloys
tags        : LeetCode Medium Array BinarySearch
---
周賽363。本來以為很難搞，看到後面發現只能選一台機器，那就簡單了。  

## 題目

你開了一間合金公司，可以用各種金屬來製造合金。  
總共有n種金屬，然後你擁有k台機器。每台機器製作合金的配方都不同。  

對於第i台機器，需要composition[i][j]個金屬j。  
最初，你個擁有stock[i]個金屬i的庫存，之後可以用cost[i]的價格購買金屬i。  

輸入整數n, k, budget。  
二維整數陣列composition。  
還有整數陣列stock和cost。  

你的目標是在預算內製造出最多的合金。  
所有合金只能在同一台機器上生產。  

回傳可製造的**合金最大數量**。  

## 解法

只能選一台機器就簡單了，遍歷機器，看哪台做得最多就行。  

但是題目有給定原先庫存stock，沒辦法直接用數學算出要額外買多少金屬，只能暴力模擬。  
又但是預算budget範圍高達10^8，如果單價都是1，慢慢增加購買量肯定會超時。  

假設我們購買某些額外金屬後，可以製造出x個金屬，那肯定也可以做出小於x的任何數量。  
答案具有單調性，二分答案找到當前機器的最大製造量。  

時間複雜度O(k \* n \* log budget)。  
空間複雜度O(1)。  

```python
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans=0
        
        # for each machine
        for i in range(k): 
            
            def ok(amount): 
                cnt=0
                for j in range(n):
                    need=max(0,composition[i][j]*amount-stock[j])
                    cnt+=cost[j]*need
                return cnt<=budget
            
            # find maximum make
            lo=0
            hi=10**9
            while lo<hi: 
                mid=(lo+hi+1)//2
                if not ok(mid):
                    hi=mid-1
                else:
                    lo=mid
                    
            # update answer
            ans=max(ans,lo) 
        
        return ans
```
