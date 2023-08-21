---
layout      : single
title       : LeetCode 2824. Count Pairs Whose Sum is Less than Target
tags        : LeetCode Easy Array SortedList BinarySearch
---
雙周賽111。

## 題目

輸入長度n的整數陣列nums，以及整數target。  

求有多少數對(i, j)滿足0 <= i < j < n 且 nums[i] + nums[j] < target。  

## 解法

暴力枚舉所有數對。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in range(i+1,N):
                if nums[i]+nums[j]<target:
                    ans+=1
                    
        return ans
```

也可以從左向右枚舉j，左邊遍歷過的都是i的候補。  
題目要求nums[i]+nums[j] < target，則nums[i]的最大值就是target-nums[j]-1，用二分搜去找到最後一個符合的位置。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sl=SL()
        ans=0
        for x in nums:
            t=target-x-1
            idx=sl.bisect_right(t)-1
            ans+=idx+1
            sl.add(x)
            
        return ans
```
