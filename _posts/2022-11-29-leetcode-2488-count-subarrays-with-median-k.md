--- 
layout      : single
title       : LeetCode 2488. Count Subarrays With Median K
tags        : LeetCode Hard Array HashTable PrefixSum
---
周賽321。原本以為是什麼sorted list加上二分搜，在錯誤的方向浪費半小時，好在有即時開竅。  

# 題目
輸入長度為n的整數陣列nums，其中1\~n各出現一次，還有一個整數k。  

求nums有多少個**非空子陣列**，其中位數為k。  

注意：中位數指的是子陣列遞增排序後，位於最中間的值。若長度為偶數，則以左方的中間值為準。  
例如[2,3,1,4]的中位數為2，而[8,4,3,5,1]中位數為4。  

# 解法
有個非常關鍵的要素：陣列中每個數字只會出現一次。如此一來，中心點的k就只有一個。  
為了使k處於排序後子陣列的正中間，除了k以外的元素必定需要x個小於k，且x大於k，否則；對於偶數長度的情況，則需要x的小於k的數，及x+1個大於k的數。  

窮舉以k為中心向左延伸的子陣列，其大於/小於k的數差值為多少，並記錄到雜湊表ld中；同理，窮舉右方差值記錄到雜湊表rd中。  
例如大於k的數有3個，小於k的數有2個，則差值為1，代表大於k的數多一個。則此陣列能夠和右方差值為-2或是-1的子陣列組成中位數為k的子陣列。  

最後窮舉左右方的差值，窮舉所有符合的左右差值，根據乘法原理加至答案中。  
> k=3, nums = [1,2,3,4,5,6]  
> 其中左子陣列[1,2]差值為-2  
> 分別可以和右子陣列[4,5]或[4,5,6]搭配  
> 得到[1,2,3,4,5],[1,2,3,4,5,6]   

注意，k的左右方也可以是空陣列，所以差值為0的數量要加上1。  
找k的位置要遍歷一次nums，計算大小差值再一次，時間為O(N)。最差情況下k位於陣列正中間，且陣列已經排序，每個差值都只會出現一次，空間O(N)。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N=len(nums)
        ans=0
        pos=nums.index(k)
        ld=Counter()
        ld[0]+=1
        rd=Counter()
        rd[0]+=1
        
        diff=0
        for i in reversed(range(pos)):
            if nums[i]>k:
                diff+=1
            else:
                diff-=1
            ld[diff]+=1
            
        diff=0
        for i in range(pos+1,N):
            if nums[i]>k:
                diff+=1
            else:
                diff-=1
            rd[diff]+=1

        for k,v in ld.items():
            ans+=v*rd[-k]
            ans+=v*rd[-k+1]
            
        return ans
```

也可以省略一個雜湊表，只存左邊差值，在計算右邊差值的時候直接更新答案。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N=len(nums)
        pos=nums.index(k)        
        ans=0
        d=Counter()
        d[0]+=1
        diff=0
        for i in reversed(range(pos)):
            if nums[i]>k:
                diff+=1
            else:
                diff-=1
            d[diff]+=1
        
        ans+=d[0]
        ans+=d[1]
        diff=0
        for i in range(pos+1,N):
            if nums[i]>k:
                diff+=1
            else:
                diff-=1
            ans+=d[-diff]
            ans+=d[-diff+1]
            
        return ans
```