--- 
layout      : single
title       : LeetCode 2426. Number of Pairs Satisfying Inequality
tags        : LeetCode Hard Array Math BinarySearch SortedList
---
雙周賽88。要不是Q1罰我15分鐘，本來應該會有400名左右，可惜了。  

# 題目
輸入兩個長度為n的整數陣列nums1和nums2，以及一個整數diff。  
找到符合以下規則的數對(i, j)：  
- 0 <= i < j <= n - 1  
- nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff  

返回滿足條件的對數。  

# 解法
原來這條公式需要列舉出i,j才能算出是否合法，非常難處理，但只要進行移項就會簡化很多。  
> nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff  
> 移項把i和j放到同一邊  
> nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff  

因為i一定小於j，所以從小到大列舉j時，先前出現過的索引都可以做為i。直接用二分搜找到有多少i可以使等式成立，根據乘法公式加入答案裡面即可。  

```python
from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sl=SortedList()
        ans=0
        
        for n1,n2 in zip(nums1,nums2):
            target=n1-n2+diff
            idx=sl.bisect_right(target)
            ans+=idx
            sl.add(n1-n2)
            
        return ans
```
