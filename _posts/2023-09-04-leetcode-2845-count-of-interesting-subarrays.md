---
layout      : single
title       : LeetCode 2845. Count of Interesting Subarrays
tags        : LeetCode Medium Array PrefixSum HashTable
---
周賽361。一直糾結怎麼nums[i]跟k跟modulo三者間有什麼奇妙關係，沒想出來怎麼做，要掉大分了。  

## 題目

輸入整數陣列nums，還有整數modulo和k。  

你的目標是計算有幾個子陣列是**有趣的**。  

一個**有趣的**子陣列nums[l..r]必須符合：  

- 介於[l, r]區間內，設cnt為滿足nums[i] % modulo == k的個數。且cnt % modulo == k  

求有多少**有趣的**子陣列。  

## 解法

拆成兩個階段比較好理解。  

1. 把nums中符合nums[i]%modulo==k的位置改成1，否則改成0  
2. 找到nums有幾個子陣列總和模modulo後餘數為k  

利用前綴和的思想，從左向右遍歷nums，並維護變數ps做前綴和。  
先不管modulo，假設當前nums[0..i]的ps是5，但是目標k=2，所以要扣掉前綴和為ps - k = 3的子陣列nums[0..j]。  
承上例，如果modulo為5，做完模運算後的ps會變成0。這時ps-k = -2，和3一樣對5同餘，所以可扣掉任何模modulo後餘數為3的子陣列。  
當然扣掉空子陣列也是一種選擇，記得初始化餘0的子陣列計數為1。  

時間複雜度O(N)。  
空間複雜度O(min(N, modulo))。  

```python
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ps=0
        d=Counter()
        d[0]=1
        ans=0
        
        for x in nums:
            if x%modulo==k:
                ps+=1
                ps%=modulo
            ans+=d[(ps-k)%modulo]
            d[ps]+=1
            
        return ans
```
