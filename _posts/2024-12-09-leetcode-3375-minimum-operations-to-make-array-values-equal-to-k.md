---
layout      : single
title       : LeetCode 3375. Minimum Operations to Make Array Values Equal to K
tags        : LeetCode Easy Simulation Greedy HashTable
---
biweekly contest 145。

## 題目

輸入整數陣列 nums 和整數 k。  

若一個陣列中所有**嚴格大於** h 的值都**相等**，則稱 h 是**合法的**。  

例如：nums = [10, 8, 10, 8]，則 h = 9 是合法的，因為所有大於 9 的值都是 10；但 5 不是合法的。  

你可以對 nums 執行以下操作：  

- 選擇整數 h，且 h 在**當前** nums 中是合法的。  
- 對於所有所隱 i，若滿足 nums[i] > h，則把 nums[i] 改成 h。  

求使得 nums 中所有元素變成 k 的**最小**操作次數。若不可能則回傳 -1。  

## 解法

講得很囉唆，整理一下：  

- h 必須小於 nums 的最大值。  
- 操作相當於把所有最大值變小。  

操作只能把元素變小，如果 nums 最小值小於 k，則不可能有答案。  

雖然沒限制 h 是否需在 nums 中，但為了操作次數盡可能少，每次操作應選擇**次大值**作為 h。  
操作內容也就是把最大值變成次大值。不斷重複，直到只剩下一種元素為止。  

但最後剩下的元素可能不是 k，所以還需要再操作一次變成 k。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set(nums)

        if min(s) < k:
            return -1

        ans = 0
        while len(s) > 1:
            ans += 1
            s.remove(max(s))

        if k not in s:
            ans += 1

        return ans
```
