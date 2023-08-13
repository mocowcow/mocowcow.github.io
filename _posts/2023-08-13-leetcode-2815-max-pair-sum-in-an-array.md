---
layout      : single
title       : LeetCode 2815. Max Pair Sum in an Array
tags        : LeetCode Easy Array Simulation
---
周賽358。這題目原文就有點難看懂，例題也不太好，要翻成中文也很難描述。  

## 題目

輸入整數陣列nums。  
你必須從nums中找到**總和最大**的數對，其中兩個數所出現的最大**數字**必須相同。  

若沒有答案則回傳-1。  

## 解法

一個數出現的最大數字，指的是把每個位數拆開後，其中的最大值。  
例題給的71和17，不如改成71和27更加容易理解。  

總之先預處理所有數的**最大數字**。窮舉所有數對，若最大數相同，則以總和更新答案。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        N=len(nums)
        
        def f(x):
            mx=0
            while x>0:
                mx=max(mx,x%10)
                x//=10
            return mx
        
        digit=[f(x) for x in nums]
        ans=-1
        for i in range(N):
            for j in range(i+1,N):
                if digit[i]==digit[j]:
                    ans=max(ans,nums[i]+nums[j])
                    
        return ans
```

對於每個最位數只需要維護最大的值，也就是0\~9共10種。  
在遍歷nums中的每個數字x時，直接和**最大數字相同**的**最大數**加總，以此更新答案。  

時間複雜度O(N log MX)，其中MX為max(nums)。  
空間複雜度O(1)。  

```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:

        def f(x):
            mx=0
            while x>0:
                mx=max(mx,x%10)
                x//=10
            return mx
        
        digit=[-inf]*10
        ans=-1
        for x in nums:
            d=f(x)
            ans=max(ans,x+digit[d])
            digit[d]=max(digit[d],x)
            
        return ans
```
