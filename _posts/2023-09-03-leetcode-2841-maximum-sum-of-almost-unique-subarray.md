---
layout      : single
title       : LeetCode 2841. Maximum Sum of Almost Unique Subarray
tags        : LeetCode Medium Array HashTable SlidingWindow TwoPointers
---
雙周賽112。

## 題目

輸入整數陣列nums和兩個正整數m跟k。  

求nums中長度為k的**幾乎唯一**子陣列的**最大總和**。若不存在則回傳0。  

若一個子陣列至少包含m種不同的元素，則稱為**幾乎唯一**。  

## 解法

很單純的滑動窗口題。維護一個大小為k的窗口，並維護總和sm，還有窗口內元素出現次數。  
如果內含大於等於m種元素，則以sm更新答案。  

時間複雜度O(N)。  
空間複雜度O(k)。  

```python
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans=0
        left=0
        sm=0
        d=Counter()
        for right,x in enumerate(nums):
            d[x]+=1
            sm+=x
            if right-left+1==k:
                if len(d)>=m:
                    ans=max(ans,sm)
                d[nums[left]]-=1
                if d[nums[left]]==0:
                    del d[nums[left]]
                sm-=nums[left]
                left+=1
                
        return ans
```
