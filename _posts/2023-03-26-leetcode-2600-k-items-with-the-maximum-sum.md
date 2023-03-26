--- 
layout      : single
title       : LeetCode 2600. K Items With the Maximum Sum
tags        : LeetCode Easy Array Math
---
周賽338。糟透了，周賽開始後40分鐘幾乎整個網站都是掛掉的。  

# 題目
背包裡面有一些物品，每個物品都標著1, 0或-1。  

輸入四個**非負**整數numOnes, numZeros, numNegOnes和k。  

背包裡面有：  
- numOnes個物品寫著1  
- numZeroes個物品寫著0  
- numNegOnes個物品寫著-1  

你要拿k個物品。求物品上所標的數字**最大總和**為多少。  

# 解法
優先拿1的，不夠再來拿0，最後才拿-1。  

三種物品最多各50個，最多也才150而已，直接把三種物品依序塞入陣列，回傳前k個總和。  

時空間複雜度O(numOnes + numZeros + numNegOnes)。  

```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        a=[1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        return sum(a[:k])
```

最佳解應該直接和三個數取最小值，不可拿超過k的量。  

時空間複雜度O(1)。  

```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        delta=1
        for x in [numOnes,numZeros,numNegOnes]:
            take=min(k,x)
            k-=take
            ans+=take*delta
            delta-=1
            
        return ans
```
