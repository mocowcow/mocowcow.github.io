--- 
layout      : single
title       : LeetCode 2670. Find the Distinct Difference Array
tags        : LeetCode Easy Array HashTable PrefixSum
---
周賽344。

# 題目
輸入長度n的陣列nums。  

長度同為n的陣列diff是陣列nums的**獨特差**，其中diff[i]等於前綴nums[0,...,i]中獨特元素個數**減掉**後綴nums[i+1,...,n-1]中獨特元素個數。  

回傳nums的**獨特差陣列**。  

# 解法
暴力法，直接把前後綴用set去重求獨特的個數，大小相減得到差值。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[]
        
        for i in range(N):
            pref=set(nums[:i+1])
            suff=set(nums[i+1:])
            ans.append(len(pref)-len(suff))
            
        return ans
```

上面的python一行版本。  

```python
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i+1]))-len(set(nums[i+1:])) for i in range(len(nums))]
```

最佳解應是前後綴分解，預處理前綴和後綴中的獨特元素數量，供之後O(1)時間查詢。  
之後才遍歷所有i，求[0,i]中的獨特數量-[i+1,n-1]中的獨特數量，即prefix[i]-suffix[i-1]。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        N=len(nums)
        pref=[0]*N
        suff=[0]*(N+1)
        
        # build prefix
        cnt=[0]*51
        prev=0
        for i in range(N):
            x=nums[i]
            cnt[x]+=1
            pref[i]=prev+(cnt[x]==1)
            prev=pref[i]
            
        # build suffix
        cnt=[0]*51
        prev=0
        for i in reversed(range(N)):
            x=nums[i]
            cnt[x]+=1
            suff[i]=prev+(cnt[x]==1)
            prev=suff[i]

        ans=[]
        for i in range(N):
            diff=pref[i]-suff[i+1]
            ans.append(diff)
            
        return ans
```