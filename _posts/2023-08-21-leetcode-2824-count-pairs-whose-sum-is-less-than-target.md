---
layout      : single
title       : LeetCode 2824. Count Pairs Whose Sum is Less than Target
tags        : LeetCode Easy Array SortedList BinarySearch Sorting TwoPointers
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

我們只在乎任意兩數的總和，不在乎其原始位置。  
將nums排序後，以雙指針維護兩數的位置，如果nums[lo]+nums[hi]小於target，代表nums[lo]配上nums[lo+1,hi]之間的所有數都可以滿足；若大於等於target則將hi左移。  

瓶頸在於排緒，時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        N=len(nums)
        nums.sort()
        ans=0
        lo=0
        hi=N-1
        
        while lo<hi:
            if nums[lo]+nums[hi]<target:
                # nums[lo] can match any nums[i]
                # where lo+1 <= i <= hi
                ans+=hi-(lo+1)+1 
                lo+=1
            else:
                hi-=1
                
        return ans
```
