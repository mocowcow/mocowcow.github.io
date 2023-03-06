--- 
layout      : single
title       : LeetCode 2584. Split the Array to Make Coprime Products
tags        : LeetCode Hard Array Math HashTable
---
周賽335。最近Q3常常比Q4還難，而且本來是Medium，賽後被改成Hard了。  

# 題目
輸入長度為n的整數陣列nums。  

如果在索引i**分割**陣列，其中0 <= i <= n-2，使得前i+1個元素乘積和剩下元素的乘積互質，則認為是**有效的**。  
- 例如nums=[2,3,3]，則在i=0處的切割是有效的，因為2和9互質；而在i=1則無效，因為6和3不互質；且不可於i=2分割  

求有效分割的**最小**索引i，如果不存在有效分割，則回傳-1。  

注意：只有當gcd(v1,v2)等於1時，才代表v1和v2兩數互質。  

# 解法
兩數要互質必定不可以有**公因數**。但是nums[i]範圍高達10^6，可以先**質因數分解**，方便檢查。  

質因數分解完後，紀錄每個質因數的**最後出現位置**。
從左開始遍歷每個位置i，如果所有質因數出現位置都小於等於i，則代表前綴的乘積和後綴的乘積互質，答案為i。  

時間複雜度O(N \* sqrt(max(nums)))。空間複雜度O(P)，其中P為max(nums)以內的質數個數。  

```python
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:

        def f(x):
            div=2
            fact=set()
            while div*div<=x:
                while x%div==0:
                    fact.add(div)
                    x//=div
                div+=1
            if x>1:
                fact.add(x)
            return fact
        
        N=len(nums)
        last={}
        for i,n in enumerate(nums):
            for p in f(n):
                last[p]=i
        
        end=0
        for i in range(N-1):
            for p in f(nums[i]):
                if last[p]>end:
                    end=last[p]
            if end==i:
                return i
        
        return -1
```
