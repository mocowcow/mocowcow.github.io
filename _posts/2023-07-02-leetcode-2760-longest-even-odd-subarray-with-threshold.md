--- 
layout      : single
title       : LeetCode 2760. Longest Even Odd Subarray With Threshold
tags        : LeetCode Easy Array
---
雙周賽352。這題是真的囉嗦，完全不想考慮非暴力以外的方法。  

# 題目
輸入整數陣列nums和整數threshold。  

找到最長的子陣列，其始於索引l，止於索引r，滿足0 <= l <= r < nums，並且符合以下條件：  
- nums[l] % 2 == 0  
- 對於所有介於[l, r - 1]的索引i，滿足nums[i] % 2 != nums[i + 1] % 2  
- 對於所有介於[l, r]的索引i，滿足nums[i] <= threshold  

求滿足以上條件的**最長子陣列**長度。  

# 解法
暴力窮舉所有子陣列，並檢查是否符合條件。  

只有在子陣列長度大於當前最長長度ans時，才去檢查是否合法，可以加速不少。  

時間複雜度O(N^3)。  
空間複雜度O(N)。  

```python
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        def ok(a):
            if a[0]%2!=0:
                return False
            for x in a:
                if x>threshold:
                    return False
            for x,y in pairwise(a):
                if x%2==y%2:
                    return False
            return True
        
        N=len(nums)
        ans=0
        for l in range(N):
            for r in range(l,N):
                # if ok(nums[l:r+1]):
                #     ans=max(ans,r-l+1)
                if r-l+1>ans and ok(nums[l:r+1]):
                    ans=r-l+1
                    
        return ans
```
