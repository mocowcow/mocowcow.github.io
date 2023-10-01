---
layout      : single
title       : LeetCode 2875. Minimum Size Subarray in Infinite Array
tags        : LeetCode Medium Array SlidingWindow TwoPointers Math
---
周賽365。最近被modulo搞了一百次，這回直接本能反應過來。  

## 題目

輸入整數陣列num，還有整數target。  

陣列infinite_nums是由無數個num所組成，也就是num + num + ...。  

求總和等於target的子陣列，其**最短長度**多少。若不可能，則回傳-1。  

## 解法

這個無限陣列聽起來有點像循環陣列，馬上想到將nums頭尾相接，在裡面滑動窗口找target。  

假設nums總和為tot，而target超大，甚至超過tot的兩倍怎麼辦？這樣頭尾相接也不夠。  
這種情況下需要好幾個完整的nums，在加上nums其中某一段子陣列(或是頭尾兩段)。  

可以直接用target/tot求需要多少個完整nums，而某段子陣列就是target%tot。  
最後在循環nums中找到長度最小的target%tot子陣列，找不到就是-1。

時間複雜度O(N)。  
空間複雜度O(N)。

```python
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N=len(nums)
        tot=sum(nums)
        rep,t=divmod(target,tot)
        
        a=nums*2
        sm=0
        ans=inf
        left=0
        for right,x in enumerate(a):
            sm+=x
            while sm>t:
                sm-=a[left]
                left+=1
            if sm==t:
                ans=min(ans,right-left+1)
                
        if ans==inf:
            return -1
        
        return ans+N*rep
```

也可以不複製貼上整個nums，改用modulo處理滑動窗口的索引，可以省不少空間。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N=len(nums)
        tot=sum(nums)
        rep,t=divmod(target,tot)
        
        sm=0
        ans=inf
        left=0
        for right in range(N*2):
            sm+=nums[right%N]
            while sm>t:
                sm-=nums[left%N]
                left+=1
            if sm==t:
                ans=min(ans,right-left+1)
                
        if ans==inf:
            return -1
        
        return ans+N*rep
```
