---
layout      : single
title       : LeetCode 287. Find the Duplicate Number
tags 		: LeetCode Medium Array BinarySearch TwoPointers
---
每日題。以前還真沒發現可以雙指標解。

# 題目
輸入長度為N+1的數列nums，裡面只會出現1~N的數字，但是有其中一個數字會出現兩次以上。  
求不修改nums且只使用O(1)的解法。

# 解法
二分搜還是需要一點心眼才能想到，畢竟nums不是有序數列，但是說了1~N大部分數字只會出現一次，若1\~x沒有重複的話，總數一定不超過x個。  
基於上述判斷，如果1~mid不足mid個，代表重複數一定大於mid，更新下界為mid+1；否則重複數小於等於mid，更新上界為mid。

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo=1
        hi=len(nums)-1
        while lo<hi:
            mid=(lo+hi)//2
            cnt=0
            if sum(n<=mid for n in nums)<=mid:
                lo=mid+1
            else:
                hi=mid
                
        return lo
```

還有雙指標解法，一早解完精神都來了。  
長度為N，出現的數最大為N-1，剛好可以看成一個單向linked list。如nums[0]=1，代表0的下一格走向1。而一定有某點存在多個進入點，造成循環。  
設出發點到循環入口E的距離為a，E到相遇點M的距離為b，M回到E的入口為c。  
先用快慢指標找到相遇點M，相遇時fast走過的距離為a+b+c+b，slow走過的距離為a+b，**因為fast為slow兩倍速**，可得(a+b)*2=a+b+c+b，確定a=c。  
所以相遇點M再走c步(其實就是a步)可以回到入口E。分別從起點和M點以相同速度出發，相遇時剛好走完c步(a步)，回傳入口E。

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find meet point
        fast=slow=nums[0]
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if fast==slow:
                break
            
        # find cycle entrance
        fast=nums[0]
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]
                
        return slow
```