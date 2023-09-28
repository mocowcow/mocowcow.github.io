---
layout      : single
title       : LeetCode 2855. Minimum Right Shifts to Sort the Array
tags        : LeetCode Easy Array Sorting Simulation
---
雙周賽113。

## 題目

輸入長度n，由**不同**正整數組成的陣列nums。  
求使得nums有序所需的**最少右移次數**，若不可能則回傳-1。  

**右移**指的是將所有位於i的元素移動至(i+1)%n。  

## 解法

數據範圍小，照常暴力解決。  

對於長度n的陣列來說，只有n種有效的移動結果，也就是右移0\~n-1次。  
先找到nums排序後的結果，依次模擬nums右移，若等同於排序則回傳當前次數。  

時間複雜度O(n^2)。  
空間複雜度O(n)。  

```python
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        N=len(nums)
        a=sorted(nums)
        
        if a==nums:
            return 0
        
        for i in range(1,N):
            t=nums.pop()
            nums=[t]+nums
            if nums==a:
                return i
            
        return -1
```

如果能透過右移使得nums有序，則代表他本來就是有序，只是先前被右移了數次。  
這種情況下nums會形成兩段遞增的子陣列，例如[3,4] + [1,2]。  

此外，右段的最後一個數不得大於左段的第一個數，否則整個陣列不可能有序。  
例如[3,4] + [2,4]則不合規則。  

同時符合以上兩點，右半的長度則等於需要右移的次數。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        N=len(nums)
        
        # find first increasing part
        i=0
        while i+1<N and nums[i]<=nums[i+1]:
            i+=1
        
        # already sorted
        if i==N-1:
            return 0
        
        # find second increasing part
        i+=1
        i0=i
        while i+1<N and nums[i]<=nums[i+1]:
            i+=1
        
        # more than 2 part
        if i!=N-1:
            return -1
        
        if nums[0]<nums[-1]:
            return -1

        # shift second part to front side
        # [i0, N-1]
        return N-1-i0+1
```
