---
layout      : single
title       : LeetCode 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
tags 		: LeetCode Medium Array Sorting Greedy
---
滿符合我電波的題目，一看到就秒殺，不錯有趣。

# 題目
輸入整數陣列nums。每次動作，你可以將其中任意元素改變成任意數值。求三次動作後，可以將數列中最大數和最小數的差值**最小化**到多少。

# 解法
說到最大最小數，第一個想法當然是排序了。  
將任意元素改值，基本上可以當作把他刪掉，讓他不影響差值。要使差值最小化，無非兩個方向：把上限降低、把下限提高。  
如此一來就可以透過窮舉來計算最佳解：  
> 總共三次動作，有以下組合  
> 1. 下限提高3次  
> 2. 下限提高2次，上限降低1次  
> 3. 下限提高1次，上限降低2次  
> 4. 上限降低3次  

取最小的方案，答案就出來了。  
不要急，看看測資，nums長度最小只有1，現在提交就會噴BUG。  
因為我們可以行動3次，如果長度3以下，都可以將其改成相同值，差值可以降到0。如果長度為4，還是可以將三個數刪掉，最大值同時等於最小值，差值還是0。  
回到上方加入edge case的處理，長度小於等於4，直接回傳0。


```python
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        N=len(nums)
        if N<=4:
            return 0
        
        ans=math.inf
        for lpop in range(0,4):
            rpop=3-lpop
            a=nums
            ans=min(ans,nums[N-1-rpop]-nums[0+lpop])
            
        return ans
            
```

