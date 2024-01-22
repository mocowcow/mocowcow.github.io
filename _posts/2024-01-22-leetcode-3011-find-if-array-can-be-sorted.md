---
layout      : single
title       : LeetCode 3011. Find if Array Can Be Sorted
tags        : LeetCode Medium Array BitManipulation TwoPointers
---
雙周賽122。又是分組循環，這個技巧真的好用。  

## 題目

輸入長度 n 的正整數陣列 nums。  

每次操作，你可以將任意兩個相鄰、且擁有相同**設置位**數量的元素交換。  
你可以執行任意次操作(包含零次)。  

如果可以將陣列排序，回傳 true；否則回傳 false。  

## 解法

**設置位**指的是一個數字的二進制中，裡面有多少個 1 位元。  

若有數個**連續相鄰**的元素，其設置位數量都是 x，則可以進行若干次交換來得到任何排序方式。  
反之，不同設置位數的元素不可交換，形成一個邊界。因此可以將 nums 以設置位數來分組，得到若干個互不影響的子陣列。  
例如：  
> nums = [8,4,2,30,15]  
> 8,4,2 都只有 1 個設置位  
> 30,15 都有 2 個設置位  
> 因此分成 [8,4,2], [30,15] 兩組  

分組後，將各組分別排序(也可以只找最大最小值)，確保當前組別的**最小值**必須大於等於上一組的**最大值**即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        last = 0
        i = 0
        while i < N:
            # group by same set bit count
            j = i
            cnt = nums[i].bit_count()
            while j+1 < N and nums[j+1].bit_count() == cnt:
                j += 1
            
            # check if sorted
            sub = nums[i:j+1]
            if min(sub) < last:
                return False
            # go next group
            last = max(sub)
            i = j + 1
            
        return True
```
