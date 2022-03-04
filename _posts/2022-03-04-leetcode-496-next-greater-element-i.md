---
layout      : single
title       : LeetCode 496. Next Greater Element I
tags 		: LeetCode Easy Array Math Geometry
---
Study Plan - Programming Skills。  

# 題目
不重複整數陣列nums1和nums2，nums1為nums2的子集合。求nums1中每個整數n在nums2中往右遇到第一個**比n更大的數**為多少；若無則為-1。  

# 解法
因為num2都是往右邊找，也有可能左方多個數共用同一個**更大數**。  
維護堆疊st，遍歷nums2所有數n，若堆疊最上方的數小於當前的n，則該數的**更大數**為n，保存至雜湊表gt。  
最後遍歷nums1所有數，試著從gt裡面找處理完的**更大數**，找不到則回傳-1。

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ans=[]
        gt={}
        
        for n in nums2:
            while st and n>st[-1]:
                gt[st.pop()]=n
            st.append(n)
            
        for n in nums1:
            if n in gt:
                ans.append(gt[n])
            else:
                ans.append(-1)
                
        return ans
```
