--- 
layout      : single
title       : LeetCode 2439. Minimize Maximum of Array
tags        : LeetCode Medium Array PrefixSum BinarySearch
---
雙周賽89。挺難的，可能比某些簡單的Q4還難，雖然我有做出來，但不是最佳解。  

# 題目
輸入由n個非負整數組成陣列nums。  

在一次操作中，你必須：  
- 選擇一個整數i，其中1 <= i < n且nums[i] > 0  
- 將nums[i]減1  
- 將nums[i-1]加1  

在執行任意次操作後，回傳**nums中最大整數**的**最小可能值**。  

# 解法
簡單來說，每次動作可以把索引0以外的數字往左搬。盡可能往左邊塞，使得nums的值平均分配。  
雖然我隱約覺得有O(N)的方法，可以從左往右遍歷nums，動態更新最大值，但我一時想寫不出來。  

退而求其次，使用函數二分搜來找到可能的最小值。  
最佳情況是nums中全都是0，所以下界為0；最差情況是nums中全都是10^9，所以上界為10^9。  
定義函數canDo(x)，代表是否能使nums中所有元素都不超過x。如果mid(x)失敗，更新下界為；否則更新上界。  
重點是canDo(x)的實作，從左往右遍歷所有nums[i]，在某索引i時，共有i+1個元素，所以這些元素的總和上限應該為x*(i+1)。若總和超過上限，則代表陣列中最大值必定超過x，回傳false；若全部i的平均都不超過x，則最後回傳true。  

每次canDo的時間是O(N)，二分搜需要進行log(10^9)次，時間複雜度為O(N log 10^9)。因為要計算nums前綴和，空間複雜度O(N)。  

```python
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        N=len(nums)
        ps=list(accumulate(nums))
        
        def canDo(x):
            for i,n in enumerate(ps):
                if n>x*(i+1):
                    return False
            return True
        
        lo=nums[0]
        hi=10**9
        while lo<hi:
            mid=(lo+hi)//2
            if not canDo(mid):
                lo=mid+1
            else:
                hi=mid
        
        return lo
```
