---
layout      : single
title       : LeetCode 2134. Minimum Swaps to Group All 1's Together II
tags 		: LeetCode Medium SlidingWindow Array
---
模擬周賽275。花了不少時間想該用什麼演算法。

# 題目
輸入一個只會出現0或1的陣列nums，其頭尾是相連的。你可以任意選擇兩個位置進行交換，最少需要多少次交換才能把所有的1連在一起。

# 解法
一開始只覺得能換的方式很多，到底要怎樣才知道換到哪。後來看到測資N<=10^5，八成是要O(N)的演算法，最後才驚覺要用滑動視窗。  
先計算陣列中總共出現幾次1，記為cnt1，就能確定視窗大小。從頭滑到尾，右進左出，每次以(cnt1-視窗內1)更新答案。因為頭尾相連，所以長度要在加上視窗大小，這樣剛好可以跑完所有位置。

例：  
> nums = [1,1,0,0,1] 視窗大小為3 答案為0  
> [(1,1,0),0,1] 需交換1次  
> [1,(1,0,0),1] 需交換2次   
> [1,1,(0,0,1)] 需交換2次  
> [1),1,0,(0,1] 需交換2次  
> [1,1),0,0,(1] 需交換0次  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        cnt1 = sum(nums)
        window = 0
        # init window
        for i in range(cnt1):
            window += nums[i]
        ans = cnt1-window
        # count swap
        for i in range(cnt1, N+cnt1):
            window += nums[i % N]
            window -= nums[(i-cnt1) % N]
            ans = min(ans, cnt1-window)

        return ans
```
