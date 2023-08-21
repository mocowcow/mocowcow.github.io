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

最佳解還是滑動窗口，但不需要二分。  

一個**同等的**子陣列需要由相同元素組成，先將索引i依照nums[i]的值分組。  
對於每個組單獨處理，假設一個組v之中包含了索引[1,3,5]，我們可以知道nums[1,5]這個子陣列中共有5個元素，其中3個元素相同，剩下5-3=2個是必須被刪除的。  
如果需要被刪除的個數超過k，則嘗試縮減左邊界，直到不超過k為止。這時後再以相同元素的個數更新答案。

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        d=defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
            
        ans=1
        for v in d.values():
            left=0
            for right,x in enumerate(v):
                while True:
                    tot=v[right]-v[left]+1
                    good=right-left+1
                    bad=tot-bad
                    if bad<=k:
                        break
                    left+=1
                ans=max(ans,good)
                
        return ans
```
