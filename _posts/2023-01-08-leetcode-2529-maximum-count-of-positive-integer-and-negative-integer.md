--- 
layout      : single
title       : LeetCode 2529. Maximum Count of Positive Integer and Negative Integer
tags        : LeetCode Easy Array BinarySearch
---
周賽327。

# 題目
輸入**非遞減**排序的整數陣列nums，求正數和負數**個數**中的最大值。  
換句話說，如果nums中有pos個正數和neg個負數，回傳pos和neg兩者中的最大值。  

注意：0不是正數也不是負數。  

# 解法
直接統計正負數，然後回傳最大值。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=neg=0
        for n in nums:
            if n>0:
                pos+=1
            elif n<0:
                neg+=1
                
        return max(pos,neg)
```

一行版本。  

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(1 for n in nums if n>0),sum(1 for n in nums if n<0))
```

上面方法沒有利用到陣列的**有序**特性，可以透過二分搜找到**最後一個負數**以及**最後一個0**的位置，直接計算正負個數。  

時間複雜度O(log N)。空間複雜度O(1)。  

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N=len(nums)
        last_neg=bisect_left(nums,0)-1
        last_zero=bisect_right(nums,0)-1
        
        neg=last_neg+1
        pos=N-(last_zero+1)
        
        return max(neg,pos)
```