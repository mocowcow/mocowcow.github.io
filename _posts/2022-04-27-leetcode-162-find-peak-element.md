--- 
layout      : single
title       : LeetCode 162. Find Peak Element
tags        : LeetCode Medium Array BinarySearch
---
二分搜學習計畫。不太直覺但是很剛好可以二分搜的題目，而且因為測資很小，導致暴力法跑起來比二分搜還快。

# 題目
輸入陣列nums，找到nums中的**峰值元素**位置。  
**峰值元素**指的是某元素嚴格大於其左右鄰居，且你可以假設nums[-1]和nums[N]為無限小。若有多個峰值元素，回傳其中之一即可。

# 解法
這時候python陣列就很方便了，先找出nums長度N，之後在nums尾端加上一個無限小，如此一來nums[-1]和nums[N]剛好都會指到無限小上面。  
遍歷每個位置，哪個位置大於左右鄰居就是答案。

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N=len(nums)
        nums+=[-math.inf]
        for i in range(N):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
```

可是題目有要求使用O(log N)解法，很明顯提示二分搜，但是其中奧妙不太容易發覺。  
上下界為0和N-1，沒有問題，那麼如何依mid來做判斷縮減哪方的邊界？  
i必須要大於左右鄰居才是峰值，那我們先粗暴的以i的右鄰居做判斷：如果nums[i]小於nums[i+1]，那麼i一定不可能是峰值，直接把下界更新為mid+1去；否則i可能是峰值，上界更新為mid。  
那峰值的左鄰居怎麼確認？根據剛才的邏輯，只有在某個位置x，nums[j]小於nums[j+1]時才會收縮下界，可以保證左鄰居一定小；又或者下界沒收縮過，nums[-1]預設也是無限小。  

試著考慮[1,2,3,4]和[4,3,2,1]：  
> [1,2,3,4]  
> lo=0, hi=3, mid=1 更新下界  
> lo=2, hi=3, mid=2 更新下界  
> lo=3, hi=3 峰值為nums[3]
> [4,3,2,1]  
> lo=0, hi=3, mid=1 更新上界  
> lo=0, hi=1, mid=0 更新上界  
> lo=0, hi=0 峰值為nums[0]  

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=(hi+lo)//2
            if nums[mid]<nums[mid+1]:
                lo=mid+1
            else:
                hi=mid
        
        return lo
```