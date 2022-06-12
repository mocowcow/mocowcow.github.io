--- 
layout      : single
title       : LeetCode 1695. Maximum Erasure Value
tags        : LeetCode Medium Array SlidingWindow HashTable
---
每日題。最近sliding window的出現頻率略高，今天是連續第三天，加上昨天的雙周賽Q4也是。

# 題目
輸入正整數陣列nums，並試著刪除一個不包含重複數字的子陣列。刪除子陣列所獲得的**分數**為其元素總和。  
回傳刪除一個子陣列可以獲得的**最高分數**。  

# 解法
我們要找不包含重複數字的子陣列，且越長越好，並從這些子陣列中找到總和最大者。  

為了要確保數字不重複，維護集合seen，將出現過的數字加入。而sm則作為子陣列的總和。  
列舉每個位置的數字n作為滑動窗口的右邊界，並先檢查n是否已經出現過，若有則不斷刪除左方元素直到n消失為止。  
將n加入後，以sm更新子陣列的最大值ans。最後回傳ans就是答案。  

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans=0
        sm=0
        l=0
        seen=set()
        for n in nums:
            while n in seen:
                sm-=nums[l]
                seen.remove(nums[l])
                l+=1
            seen.add(n)
            sm+=n
            ans=max(ans,sm)
        
        return ans
```
