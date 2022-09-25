--- 
layout      : single
title       : LeetCode 2419. Longest Subarray With Maximum Bitwise AND
tags        : LeetCode Medium Array Greedy BitManipulation
---
周賽312。這題真是要了我的命，一直糾結怎麼對AND運算做復原動作，浪費了好久時間才恍然大悟。  

# 題目
輸入大小n的整數陣列nums。  
存在一個nums的非空子陣列，他有著最大的位元AND運算總和。  

換句話說，假設k是所有nums子陣列中做位元AND運算的最大值，要找到所有值為k的子陣列。  
求符合以上條件的子陣列中，最長長度為多少。  

# 解法
講這麼多，聰明的朋友應該要立刻想到，nums中不管怎麼AND運算，其子陣列最大值一定就是nums中的最大值。  
根本不用找什麼子陣列還是滑動窗口，直接找最大值mx最多連續出現幾次就好。  

先找到nums中的最大值mx，然後遍歷第二次，貪心地找由mx所連續組成的子陣列。  

時間複雜度O(N)，空間複雜度O(1)。  

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=1
        mx=max(nums)
        cnt=0
        
        for n in nums:
            if n==mx:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=0
            
        return ans
```

也可以簡化成一次遍歷，邊找最大數字，邊更新長度。  

時間複雜度O(N)，空間複雜度O(1)。  

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=1
        mx=-inf
        cnt=0
        
        for n in nums:
            if n>mx:
                mx=n
                ans=cnt=1
            elif n==mx:
                cnt+=1
            else:
                cnt=0
            ans=max(ans,cnt)
            
        return ans
```