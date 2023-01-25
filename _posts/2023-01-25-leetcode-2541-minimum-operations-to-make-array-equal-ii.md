--- 
layout      : single
title       : LeetCode 2541. Minimum Operations to Make Array Equal II
tags        : LeetCode Medium Array
---
雙周賽96。這題是真的很陷阱，就算是前段選手大概也有90%都踩到地雷。  

# 題目
輸入兩個長度為N的整數陣列nums1和nums2，以及整數k。  

你可以對nums1執行以下動作：  
- 選兩個索引i和j，使nums1[i]增加k，然後使nums2[h]減少k  

對於所有的i都滿足nums1[i]==nums2[i]，則稱nums1和nums2**相等**。  

求使得nums1和nums2**相等**的**最少操作次數**。若不可能使兩者相等則回傳-1。  

# 解法
每次nums1[i]增加，nums1[j]減少，實際上陣列中的總和並沒有改變。也就是說，若兩陣列的初始總和必須相等，否則永遠不可能達成。  

既然確定了兩陣列總和相同，那麼我們在某個索引nums1[i]少於nums2[i]的部分，一定會從某個nums1[j]扣過來；同理，若多餘的部分，也會扣掉，並加到某個地方去。  
如此一來，我們只需要判斷nums1[i]和nums2[i]的差值diff，並將diff除k，得到需要的動作次數。最後將動作次數除2，即為答案。  

需要注意的是：若差值diff無法被k整除，無論如何也不可能使兩陣列相等，直接回傳-1。  
更需要注意的是：**k有可能為0**，所以求餘運算的時候會將0當作分母引發錯誤，這時候需要單獨判定兩陣列是否相等。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1)!=sum(nums2):
            return -1
        
        if k==0:
            if nums1==nums2:
                return 0
            return -1
        
        ans=0
        for a,b in zip(nums1,nums2):
            diff=abs(a-b)
            if diff%k!=0:
                return -1
            ans+=diff//k
            
        return ans//2
```
