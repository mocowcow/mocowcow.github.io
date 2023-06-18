--- 
layout      : single
title       : LeetCode 2740. Find the Value of the Partition
tags        : LeetCode Medium Sorting
---
周賽350。又是腦筋急轉彎，這次馬上就找到重點。  

# 題目
輸入**正整數**陣列nums。  

將nums分割成兩個陣列num1和nums2，滿足：  
- 每個元素必須屬於nums1或nums2  
- 兩個陣列都**不可為空**  
- 分割值**最小化**  

分割值等於|max(nums1) - min(nums2)|。  

求最小的分割值。  

# 解法
設nums1的最大值為mx，且num2的最小值為mn。  
所有小於等於mx的數都要在nums1中，且大於等於mn的數都要在nums2中。  
但是每個元素都必須屬於nums1或nums2，所以mx和mn必須相鄰。  
以上綜合起來剛好就是排序好的陣列。  

將nums排序後，窮舉所有相鄰的數對(a,b)，即mx=a, mn=b。  
直接求差值更新答案即可。  

時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans=inf
        for a,b in pairwise(nums):
            ans=min(ans,b-a)
            
        return ans
```
