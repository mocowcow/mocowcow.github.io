--- 
layout      : single
title       : LeetCode 2540. Minimum Common Value
tags        : LeetCode Easy Array HashTable TwoPointers
---
雙周賽96。

# 題目
輸入兩個依非遞減排序的整數陣列nums1和nums2，求兩個陣列中**最小的共同整數**。若不存在共通的整數，則回傳-1。  

若一個整數分別在nums1和nums2中至少出現一次，則稱為**共同整數**。  

# 解法
把nums2轉成集合，可供O(1)查找，再來遍歷nums1中每個數字n，因為nums1已經排序過，所以碰到第一個共通整數一定是最小的，直接回傳。  

時間複雜度O(M+N)。空間複雜度O(N)，其中M為nums1長度，N為nums2長度。  

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s2=set(nums2)        
        for n in nums1:
            if n in s2:
                return n
            
        return -1
```

也可以把兩個陣列都轉成集合，使用集合的交集方法找出所有共同整數，再找出其中的最小值。  

時間複雜度O(M+N)。空間複雜度O(M+N)。  

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1)&set(nums2),default=-1)
```

以上兩種方法都沒有妥善利用到**有序**的特性，使用雙指針直接遍歷兩陣列，可以不需要額外空間，應是此題的最佳解。  

時間複雜度O(M+N)。空間複雜度O(1)。  

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        M=len(nums1)
        N=len(nums2)
        i=j=0
        
        while i<M and j<N:
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
                
        return -1
```