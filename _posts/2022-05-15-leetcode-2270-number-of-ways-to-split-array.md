--- 
layout      : single
title       : LeetCode 2270. Number of Ways to Split Array
tags        : LeetCode Medium Array PrefixSum
---
雙周賽78。聽說c++有災情，一堆人沒有用long long拿到溢位WA。若我不是用python八成也會中獎。

# 題目
輸入長度為n，且索引從0開始的整數陣列nums。  
若滿足以下條件，則稱為i的有效拆分方式：  
- 前i+1個元素的總和大於等於後方n-i-1個元素的總和  
- i的右邊至少有一個元素，即是0<=i<N-1  

求有幾種有效拆分方式。

# 解法
跟[2256. minimum average difference]({% post_url 2022-05-01-leetcode-2256-minimum-average-difference %})有九成項的題目，最大的差別是這題的右方元素不可以為空。  

當nums長度為n時，會有n-1種拆分方式。  
先求nums總和當作右方元素和r，然後左方元素和l初始為0。  
遍歷nums，將nums[i]從右方扣除後，加入左方，並檢查l是否大於等於r，若是則答案+1。  

注意，右方不可為空，所以nums最尾端元素不處理。

```python
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        l=0
        r=sum(nums)
        for i in range(N-1):
            l+=nums[i]
            r-=nums[i]
            if l>=r:
                ans+=1
                
        return ans
```

其實可以只記錄左方總和l就好，因為陣列總和sm扣掉l，剩下的就是r了。  

```python
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        l=0
        sm=sum(nums)
        for i in range(N-1):
            l+=nums[i]
            if l>=sm-l:
                ans+=1
                
        return ans
```
