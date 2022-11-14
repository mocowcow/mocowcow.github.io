--- 
layout      : single
title       : LeetCode 2465. Number of Distinct Averages
tags        : LeetCode Medium Array Sorting TwoPointers
---
雙周賽91。

# 題目
輸入一個偶數長度的整數陣列nums。  

重複以下步驟直到nums為空為止：  
- 找到並刪除nums中的最小數字  
- 找到並刪除nums中的最大數字 
- 計算兩個被刪除數字的平均值  

a和b兩數的平均值為 (a + b) / 2：  
- 例如2和3平均值為 (2 + 3) / 2 = 2.5  

求有多少**不重複的平均值**。  

注意，若最大或最小數有多個時，刪除任一皆可。  

# 解法
每次要使用到最大和最小值，第一個反應就該是排序。雖然暴力法也是可以，但是寫起來反而麻煩，不如乖乖排好。  

使用雙指針分別指向陣列首端的最小元素，以及尾端的最大元素，取兩者平均值後加入集合中去重複就是答案。  

```python
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s=set()
        lo=0
        hi=len(nums)-1
        
        while lo<hi:
            s.add((nums[hi]+nums[lo])/2)
            lo+=1
            hi-=1
        
        return len(s)
```

其實也不用雙指針，因為對於長度N的陣列來說，第0個元素對應到第N-1，而第i個元素對應到N-1-i，直接在迴圈內存取就可以。  

```python
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        s=set()
        
        for i in range(N):
            s.add((nums[i]+nums[N-1-i])/2)
        
        return len(s)
```