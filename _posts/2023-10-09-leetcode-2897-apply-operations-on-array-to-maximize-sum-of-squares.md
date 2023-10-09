---
layout      : single
title       : LeetCode 2897. Apply Operations on Array to Maximize Sum of Squares
tags        : LeetCode Hard Array BitManipulation Greedy
---
周賽366。個人覺得比Q3簡單很多，至少我10分鐘就做出Q4，然後一小時做不出Q3。  

## 題目

輸入整數陣列nums和**正整數**k。  

你可以執行以下操作**任意**次：  

- 選擇兩個不同的索引i和j，並同時更新兩者的值。nums[i]改成(nums[i] AND nums[j])，而nums[j]改成(nums[i] OR nums[j])  

操作結束後，從nums中選擇k個元素，計算出他們的平方和。  

求**最大**平方和。  

答案很大，先模10^9+7後回傳。  

## 解法

先看看操作有什麼特性。  
窮舉nums[i]和nums[j]的四種情況：  

- 1 0變成0 1  
- 0 1變成0 1  
- 1 1變成1 1  
- 0 0變成0 0  

只有一種實質效果，就是讓1位元**換位**。  

試想以下例子：  
> nums = [0b101, 0b010]  
> i = 0, j = 1  
> 操作後nums = [0b000, 0b111]  
> 發現所有1位元都被集中了  

再舉其他例子：  
> nums = [0b101, 0b110]  
> i = 0, j = 1  
> 操作後nums = [0b100, 0b111]  
> 同樣1位元被集中，但是1位元總數不變  

這代表我們可以在所有元素中，在同一個位上可以任意分配現有的1位元。  

那如何使平方和盡可能大？  
一個數字越大，平方越大。使一個元素集中擁有更多的1位元，其平方值也越大。  

首先遍歷nums一次，統計各位上出現的1位元個數。  
然後重複k次集中位元，構造數字x：遍歷每個位，如果還有剩下的1，就分配給當前的x。構造完後將x的平方加入答案。  

時間複雜度O(N log MX)，其中MX為max(nums)。  
空間複雜度O(log MX)。  

```python
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        d=[0]*30
        for x in nums:
            for i in range(30):
                if x&(1<<i):
                    d[i]+=1
                    
        ans=0
        for _ in range(k):
            x=0
            for i in range(30):
                if d[i]>0:
                    d[i]-=1
                    x|=(1<<i)
            ans+=x*x
            ans%=MOD
            
        return ans
```
