--- 
layout      : single
title       : LeetCode 2348. Number of Zero-Filled Subarrays
tags        : LeetCode Medium Array TwoPointers
---
雙周賽83。看到子陣列就想到計算貢獻值，馬上就解出來。  

# 題目
輸入整數陣列nums，求有多少只由0組成的子陣列。  

# 解法
維護變數cnt，計算連續出現多少個0，每碰到新的0則計數+1；碰到非0則歸零。  
遍歷nums中每個數n，列舉每個n=0為結尾的子陣列數量。若當前n為0，則有cnt個子陣列以此位置結尾。  

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        cnt=0
        for n in nums:
            if n==0:
                cnt+=1
            else:
                cnt=0
            ans+=cnt
                
        return ans
```

也可以用雙指針來表示明確的子陣列範圍，由邊界計算出可能的子陣列數量。  

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l=0
        ans=0
        for r,n in enumerate(nums):
            if n!=0:
                l=r+1
            else:
                ans+=r-l+1
            
        return ans
```