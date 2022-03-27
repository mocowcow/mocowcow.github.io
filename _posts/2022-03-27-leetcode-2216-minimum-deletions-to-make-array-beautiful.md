---
layout      : single
title       : LeetCode 2216. Minimum Deletions to Make Array Beautiful
tags 		: LeetCode Medium Greedy TwoPointers
---
周賽286。尷尬，腦子還沒清醒吃了三個WA，隨便翻一下好像沒幾個人錯這麼多次...。  

# 題目
美麗陣列指的是符合以下規則的陣列：  
- 陣列長度為偶數  
- 對每個偶數的索引i，nums[i]!=nums[i+1]  

求最少刪除幾個元素才能使陣列變得美麗。被刪除的元素後方會往前移，如[2,2,3,4]刪除第一個2，變成[2,3,4]。  

# 解法
一開始想著奇偶數各一個指標每次往後+2，若相同就刪一個，後來碰到[6,6,6,1,1]這種測資就炸了，正確要刪3次，卻算錯成1次。  
正確思維應該是前後各一個指標l,r，每次若刪除則r+1，刪到l和r不相同為止，然後下一輪的l移到r+1，r移到r+2。若最後剩餘長度是奇數，則把最後一個也刪掉。

```python
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        N=len(nums)
        size=N
        ans=0
        l=0
        r=1
        while r<N:
            if nums[l]==nums[r]:
                size-=1
                ans+=1
                r+=1
            else:
                l=r+1
                r=l+1
                
        if size%2==1:
            ans+=1
            
        return ans
```

