--- 
layout      : single
title       : LeetCode 2605. Form Smallest Number From Two Digit Arrays
tags        : LeetCode Easy Array HashTable
---
雙周賽101。

# 題目
輸入兩個只包含數字1到9的陣列nums1和nums2，其中的數字都是**唯一的**。  

求最小的可能整數，使兩個陣列都**至少**包含該整數的一個數字。  

# 解法
從例題可以發現，如果兩陣列有共通的數字，則答案是一位數；否則是二位數。  

遍歷nums1和nums2所有數字的組合a和b，如果ab一樣，則直接更新答案；否則有兩種擺法，第一是a擺前面，第二是b擺前面。  

時間複雜度O(MN)。空間複雜度O(1)。  

```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans=inf
        
        for a in nums1:
            for b in nums2:
                if a==b:
                    ans=min(ans,a)
                else:
                    ans=min(ans,a*10+b,b*10+a)  
        
        return ans
```

上述方法的一行版本。  

```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        return min(a if a==b else min(a*10+b,b*10+a) for a,b in product(nums1,nums2))
```

使用集合來找兩陣列共通數字可以降低複雜度。  

如果有交集，則答案為交集中最小的數字；否則答案一定是由兩陣列中最小的數字組成。  

時間複雜度O(N+M)。空間複雜度O(N+M)。  

```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set(nums1)
        s2=set(nums2)
        union=s1&s2
        
        if union:
            return min(union)
        
        m1=min(s1)
        m2=min(s2)
        
        return min(m1*10+m2,m2*10+m1)
```