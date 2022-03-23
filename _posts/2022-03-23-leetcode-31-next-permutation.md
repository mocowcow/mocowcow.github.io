---
layout      : single
title       : LeetCode 31. Next Permutation
tags 		: LeetCode Medium String Math 
---
半年以前看了果斷跳過的題。今天突然想到和[這題](2022-03-22-leetcode-556-next-greater-element-iii.md)不是同個道理嗎？有如醍醐灌頂。

# 題目
輸入整數數列nums，依字典順序求其下一個較大的排列方式。如[1,2,3]的下一個排列為[1,3,2]。  
若已經為最大的排列順序，則回歸最小的排列方式。如[3,2,1]回歸[1,2,3]。

# 解法
和556題差別在於順序無法再增加時，把-1改成反轉數列而已。  

一樣從最後尾開始找遞減的後綴，如546**8754**。  
如果後綴開頭為0，代表已達最大順序，則反轉數列回傳；否則以**後綴左方第一個數x**和後綴裡最小且大於x的數換位。  
上例為6和7交換，得到547**8654**。最後把後綴反轉，得到5474568，即是答案。

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N=len(nums)
        # find decreasing suffix
        i=N-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        
        if i==0:
            nums[:]=nums[::-1]
            return 
        
        j=i
        while j+1<N and nums[j+1]>nums[i-1]:
            j+=1
        nums[i-1],nums[j]=nums[j],nums[i-1]
        nums[i:]=nums[i:][::-1]
```

