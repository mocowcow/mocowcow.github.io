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

2022-4-6複習。  
原本方法是計算需要刪除的次數，現在改為計算成功配對的字元數。  
left紀錄要配對數字，開始遍歷nums。如果left為空，就把n裝進left；left和n不同時，配對成功，配對數+2，left清空；left和n相同時代表要刪除n，所以不動作。  
最後長度N扣掉成功配對的數量就是要刪除的數量。

```python
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        matched=0
        left=None
        
        for n in nums:
            if left is None:
                left=n
            elif left!=n:
                matched+=2
                left=None
        
        return len(nums)-matched
```