--- 
layout      : single
title       : LeetCode 2760. Longest Even Odd Subarray With Threshold
tags        : LeetCode Easy Array TwoPointers SlidingWindow
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

枚舉左邊界，並嘗試擴展右邊界。  
在擴展右邊界的同時進行檢查，空間和時間都節省很多。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        N=len(nums)
        ans=0
        
        for left in range(N):
            if nums[left]%2==0 and nums[left]<=threshold:
                right=left
                while right+1<N and nums[right]%2!=nums[right+1]%2 and nums[right+1]<=threshold:
                    right+=1
                ans=max(ans,right-left+1)
                
        return ans
```

可以發現，當一個區間[left,right]結束擴展時，下一個區間的起點一定會大於right，因為選擇介於left和right之間的索引作為左邊界，他的右邊界都一定是right，只會得到更小的結果。  
所以可以直接left跳到right+1，實際上每個索引只會被訪問到一次。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        N=len(nums)
        ans=0
        left=0
        
        while left<N:
            if nums[left]%2==1 or nums[left]>threshold:
                left+=1
            else:
                right=left
                while right+1<N and nums[right+1]%2!=nums[right]%2 and nums[right+1]<=threshold:
                    right+=1
                ans=max(ans,right-left+1)
                left=right+1
                
        return ans
```