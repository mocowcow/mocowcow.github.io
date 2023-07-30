--- 
layout      : single
title       : LeetCode 2799. Count Complete Subarrays in an Array
tags        : LeetCode Medium Array HashTable SlidingWindow TwoPointers
---
周賽356。

## 題目

輸入由**正整數**陣列nums。  

如果一個子陣列滿足以下條件，則稱為**完整的**：

- 子陣列中**不同的**元素個數與原陣列相同  

求有多少**完整的**子陣列。  

## 解法

測資範圍不大，窮舉所有子陣列，並計算其**不同的**元素個數，若和原陣列相同則答案+1。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N=len(nums)
        dis=len(set(nums))
        ans=0
        for i in range(N):
            s=set()
            for j in range(i,N):
                s.add(nums[j])
                if len(s)==dis:
                    ans+=1
                    
        return ans
```

如果測資再大一些，上免方法就不能用了。  

長度為N的陣列中，總共有tot = N\*(N+1)/2個子陣列。  
只要找到全部的**不同元素各數**與原陣列不同的子陣列，從tot中扣掉，剩下的就是答案。  

時間複雜度O(N)。  
時間複雜度O(N)。  

```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N=len(nums)
        tot=N*(N+1)//2
        dis=len(set(nums))
        
        ans=0
        left=0
        d=Counter()
        for right,x in enumerate(nums):
            d[x]+=1
            while len(d)==dis:
                d[nums[left]]-=1
                if d[nums[left]]==0:
                    del d[nums[left]]
                left+=1
            ans+=right-left+1
                
        return tot-ans
```
