---
layout      : single
title       : LeetCode 2831. Find the Longest Equal Subarray
tags        : LeetCode Medium Array HashTable BinarySearch SlidingWindow TwoPointers
---
周賽359。難得沒有hard題我還可以拿到不錯的名次。在239X來回三四次，總算是突破2400的門檻。  

## 題目

輸入整數陣列nums和整數k。  

若一個子陣列中個所有元素都相同，則稱為**同等的**。空子陣列也視為**同等的**。  

求最多可以刪除k個元素的情況下，能得到的**最長**同等子陣列。  

## 解法

假設k次刪除後，我們可以找到長度為x的同等子陣列，那麼一定找得到長度小於x的；反之，找不到長度x，必定也找不到大於x的。  
答案具有單調性，可以二分。  

我們可以將刪除的k個元素**無視**，假裝他已經不見。也就是說，當我們要找長度為target的相同子陣列，只要在大小為target+k的區間中出現target相同元素即可。  
例如：  
> nums = [1,5,1], k = 1  
> 要找target = 2的相同子陣列  
> 實際大小size = 2+1 = 3  
> 子陣列[1,5,1]包含兩個1，滿足target  

那怎麼知道哪些數在區間中出現target次？當時還腦子還卡住一下，沒馬上想通。  
其實答案很簡單：最後被加入的元素最可能滿足target，檢查他就好。  

最差情況每個元素都不同，答案為1；最佳情況下全部元素都相同，答案為N。  
每次二分需要O(N)，共log N次，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        def ok(target):
            size=k+target
            d=Counter()
            left=0
            for right,x in enumerate(nums):
                d[x]+=1
                if d[x]==target:
                    return True
                if right-left+1>=size:
                    d[nums[left]]-=1
                    left+=1
            return False
        
        lo=1
        hi=N
        while lo<hi:
            mid=(lo+hi+1)//2
            if not ok(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
```
