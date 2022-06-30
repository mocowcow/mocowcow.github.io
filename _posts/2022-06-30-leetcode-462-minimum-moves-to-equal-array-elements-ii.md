--- 
layout      : single
title       : LeetCode 462. Minimum Moves to Equal Array Elements II
tags        : LeetCode Medium Array Sorting Math
---
每日題。一開始想錯了，想成平均數，正確應該是中位數才對。

# 題目
輸入長度n的陣列nums，求需要幾次動作才能使陣列中所有元素相同。  
每次動作，你可以任選一個元素將其+1或是-1。  

# 解法
陣列本身是無序的，得先排序，方便找到最大和最小值。  
假設nums=[1,2,3,4]，我們必須在1和4之間找到一個目標數t，將所有元素修改成t。
對[1,2,3,4]來說，不管t為多少，動作次數都是3次，那麼可以t除掉1和4，將t的候選範圍縮減到[2,3]，以此類推，正好就是中位數的定義。  

找到中位數median後，將所有元素和median的差加總就是答案。  

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        median=nums[mid]
        return sum(abs(x-median) for x in nums)
```
