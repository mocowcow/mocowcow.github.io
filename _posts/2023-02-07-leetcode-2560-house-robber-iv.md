--- 
layout      : single
title       : LeetCode 2560. House Robber IV
tags        : LeetCode Medium Array DP BinarySearch
---
周賽331。看到**打家劫舍**真是又驚又喜，經典系列又出新章！  

# 題目
街上有一些連續的房子，且每棟房子裡面都有一些錢。有一個小偷想行竊，但他**拒絕連續偷兩間相鄰**的房子。  

小偷的**本領**為其光顧的所有房子中，**錢財的最大值**。  

輸入整數陣列nums，代表著每棟房子的錢。  

另外還有整數k，代表小偷**最少**要偷k棟房子。測資保證一定能偷滿k棟。  

求小偷偷滿k棟房子，**最少**需要多少**本領**。  

# 解法
題目還算很良心，直接告訴你**最大值最小化**，那麼就是二分了。  

錢財的最小值為1，所以下界定為1。上界定為nums中的最大值，再高也沒有意義。  
如果mid無法偷滿k棟，則更新下界mid+1；否則mid以上的都可以成立，更新上界為mid。  

維護ok(limit)函數，判斷只偷最多limit錢財的房子，能不能滿足k棟。  
這次和原版打家劫舍有些不同，是計算房子的數量，而不是錢財的累積。所以每偷一棟都是+1。  
維護長度為N的dp陣列，其中dp[i]代表從0\~第i棟房為止，最多能夠偷幾棟。  
如果limit大於該棟房子的錢財，可以偷，也可以選擇不偷。偷的話就是到i-2為止的最大數量+1，不偷就是和i-1一樣；如果limit小於錢財，這棟房沒辦法偷，所以可以延續i-2或是i-1的結果。  

時間複雜度O(N log max(nums))。空間複雜度O(N)。  

```python
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        def ok(limit):
            dp=[0]*N
            for i,n in enumerate(nums):
                prev=0 if i<1 else dp[i-1]
                pprev=0 if i<2 else dp[i-2]
                if limit>=n:
                    dp[i]=max(prev,pprev+1)
                else:
                    dp[i]=max(prev,pprev)
                if dp[i]==k:
                    return True
            return False
                    
        lo=1
        hi=max(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if not ok(mid):
                lo=mid+1
            else:
                hi=mid
        
        return lo
```

而每次dp狀態轉移只會參考到前兩天的的結果，所以可以使用2個變數來疊代，不需要整個陣列。  
順便套用內建的二分搜函數。  

時間複雜度O(N log max(nums))。空間複雜度O(1)。  

```python
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        def ok(limit):
            prev=pprev=0
            for n in nums:
                curr=max(prev,pprev+(limit>=n))
                if curr==k:
                    return True
                pprev=prev
                prev=curr
            return False

        return bisect_left(range(max(nums)),True,key=ok)
```