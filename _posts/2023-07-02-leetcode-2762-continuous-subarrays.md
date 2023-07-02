--- 
layout      : single
title       : LeetCode 2762. Continuous Subarrays
tags        : LeetCode Medium Array TwoPointers SlidingWindow SortedList
---
雙周賽352。

# 題目
輸入整數陣列nums。  
若一個子陣列滿足以下條件，則稱為**連續的**：  
- 子陣列中任意兩個元素的絕對差 <= 2  

求有多少**連續的**子陣列。  

# 解法
假設有一個陣列a，最大值和最小值的差為2，則無論刪掉陣列中任何元素，必定不會使絕對差增加。  
因此只需要枚舉所有索引r作為右端點，找到與其對應的最長左端點l。這時r可以和[l,r]之間的任意索引組成**連續的**子陣列。  

使用sorted list來維護子陣列的最大、最小值。枚舉右端點r，將nums[r]加入sl，若最大值和最小值的差超過2，則不斷縮減左邊界l。  
縮減結束後，子陣列的長度為l-r+1，也就是r可以和l-r+1個左端點組成**連續的**子陣列，更新答案。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans=0
        sl=SL()
        
        l=0
        for r,x in enumerate(nums):
            sl.add(x)
            while sl[-1]-sl[0]>2:
                sl.remove(nums[l])
                l+=1
            ans+=r-l+1
            
        return ans
```
