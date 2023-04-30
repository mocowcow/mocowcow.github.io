--- 
layout      : single
title       : LeetCode 2656. Maximum Sum With Exactly K Elements
tags        : LeetCode Easy Array Simulation Math
---
雙周賽103。

# 題目
輸入整數陣列nums和整數k。  

你必須執行以下動作k次，並試將得分最大化：  
- 選擇nums中的一個元素m  
- 將m從陣列中刪除  
- 把m+1加入陣列中  
- 獲得m分  

求執行k次動作後，最多可以得到幾分。  

# 解法
每次動作都應當選擇nums中最大的元素，才能使得分最大化。而被選中的元素又會增加1，永遠都是最大的。  
直接找到最大值mx，將他加入分數後增加1，重複k次。 

時間複雜度O(N + k)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans=0
        mx=max(nums)
        
        for i in range(k):
            ans+=mx
            mx+=1
            
        return ans
```

如果k很大，不能跑迴圈模擬。  
注意到選擇的元素是mx, mx+1, mx+2...，是長度為k的等差數列，直接套梯形公式求和。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        return (mx+(mx+k-1))*k//2
```