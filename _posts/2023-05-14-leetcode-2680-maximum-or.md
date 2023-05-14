--- 
layout      : single
title       : LeetCode 2680. Maximum OR
tags        : LeetCode Medium Array Greedy PrefixSum BitManipulation
---
雙周賽104。這題有點小難度，結果我搞出的解法和大部分人都不一樣。  

# 題目
輸入大小為n的整數陣列nums，以及整數k。  
每次操作，你可以選擇一個元素並將其乘2。  

求經過最多k次操作後，nums中所有元素做OR運算後可以得到的最大值。  

# 解法
雖然說最多可以乘k次，但如果不到k次很浪費，無法使答案更大。  
再來，與其把k次分散到好幾個數上，不如全部乘同一個，才能使答案更大。  

但對某個數字x位移k次後，有可能使得某些位置的1位元消失。所以需要先記錄**各位元的1的數量**，如果x中的某個1位元是唯一一個，則位移後應該被刪除。  

計算出nums所有元素OR的值，窮舉每個數x作為位移的對象，計算出位移後的新OR值，更新答案。  

```python

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        OR=0
        cnt=[0]*30
        ans=0
        
        for x in nums:
            OR|=x
            for i in range(30):
                if x&(1<<i):
                    cnt[i]+=1
                    
        for x in nums:
            val=OR
            for i in range(30):
                if x&(1<<i) and cnt[i]==1:
                    val-=(1<<i)
            val|=(x<<k)
            ans=max(ans,val)
            
        return ans
```

更通用的作法是**前後綴分解**。  
當我們選擇i位移時，i左方的所有元素和i右方的所有元素都要做OR運算，因此先預處理前後綴的OR值。  
相似題[238. product of array except self]({% post_url 2022-09-03-leetcode-238-product-of-array-except-self %})。  

一樣窮舉i，將位移過的nums[i]和前後綴做OR，並更新答案即可。  

```python
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        N=len(nums)
        pref=[0]*N
        suff=[0]*N
        
        pref[0]=nums[0]
        for i in range(1,N):
            pref[i]=pref[i-1]|nums[i]
            
        suff[-1]=nums[-1]
        for i in reversed(range(N-1)):
            suff[i]=suff[i+1]|nums[i]
            
        ans=0
        for i in range(N):
            x=nums[i]<<k
            if i>0:
                x|=pref[i-1]
            if i+1<N:
                x|=suff[i+1]
            ans=max(ans,x)       
        
        return ans
```