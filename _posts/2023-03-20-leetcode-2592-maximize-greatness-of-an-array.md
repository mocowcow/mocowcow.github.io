--- 
layout      : single
title       : LeetCode 2592. Maximize Greatness of an Array
tags        : LeetCode Medium Array Greedy Sorting
---
雙周賽100。這次周賽真的滿有意思的，出題者八成是中國人。  
這題其實就是**田忌賽馬**。  

# 題目
You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.

We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].

Return the maximum possible greatness you can achieve after permuting nums.

輸入整數陣列nums。你可以將nums以任意順序重新排序，令排序後的陣列為perm。  

將**偉大值**定義為perm[i] > nums[i]的個數，其中0 <= i < nums.length。  

回傳重新排序後的**最大**偉大值。  

# 解法
題目只要求偉大值，而不要求輸出perm，也不要求按照nums中的原本順序，所以可以直接將nums排序。  
排序後，問題轉化成：有兩個相同的陣列a和b，要讓其中元素倆倆配對，怎樣配才能讓a[i] > b[i]的次數更多。  

如果當前a最小的數贏得了b最小的數，就直接配對，答案+1；如果贏不了，那麼盡可能消耗b的戰力，換掉b最大的數。  

時間複雜度在於排序，O(N log N)。因為拷貝了一個nums，空間複雜度O(N)。  

```python
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        a=deque(sorted(nums))
        b=deque(sorted(nums))
        ans=0
        
        while a:
            if a[0]>b[0]:
                ans+=1
                b.popleft()
                a.popleft()
            else:
                a.popleft()
                b.pop()
                
        return ans
```
