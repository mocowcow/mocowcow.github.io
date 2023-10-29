---
layout      : single
title       : LeetCode 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
tags        : LeetCode Medium Greedy
---
周賽369。題目有點小問題，說輸入正整數陣列，但0其實不是正整數。  

## 題目

輸入兩個正整數陣列nums1和nums2。

你要將兩陣列中的0都替換成**正整數**，且使得兩陣列的總和相等。  

求陣列總和的**最小值**。若兩者不可能相等，則回傳-1。  

## 解法

所有0都要被換成正數，那麼陣列替換後的最小總和就是總和+零的數量。  

將兩陣列替換後的最小值分別記做sm1和sm2。  

若sm1剛好等於sm2，直接就是答案；否則要試著將小的的那方增大。  
假設sm1小於sm2，必須找原本某個是0的數，改成與兩者的差值；若不存在0，則不可能相等，回傳-1。  
反之亦然。  

時間複雜度O(N+M)。  
空間複雜度O(1)。  

```python
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1=nums1.count(0)
        z2=nums2.count(0)
        sm1=sum(nums1)+z1
        sm2=sum(nums2)+z2
        
        if sm1>sm2:
            if z2>0:
                return sm1
            else:
                return -1
            
        if sm1<sm2:
            if z1>0:
                return sm2
            else:
                return -1

        return sm1 # sm1 == sm2
```
