---
layout      : single
title       : LeetCode 3355. Zero Array Transformation I
tags        : LeetCode Medium PrefixSum
---
weekly contest 424。  
最近差分陣列出場率很高。  

## 題目

輸入長度 n 的整數陣列 nums，還有二維陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>]。  

對於每個 queries[i]：  

- 選擇 [l<sub>i</sub>, r<sub>i</sub>] 之間的索引**子集**。  
- 將選擇的索引對應元素減 1。  

一個陣列的所有元素都等於 0，稱做**零陣列**。  

若執行所有操作後能使得 nums 變成**零陣列**，則回傳 true，否則回傳 false。  

## 解法

為了使 nums 全為 0，我們必須知道有幾個查詢可以對 nums[i] 減 1。  
至於哪個查詢減了哪些索引並不重要。  

---

遍歷每個查詢，對 [l, r] 之間所有索引計數加 1。  
區間修改會想到線段樹之類的東西，但是我們只需要再遍歷完 queries 才查詢，因此更適合**差分陣列**。  

對 queries 中所有區間做差分後，再做前綴和，檢查**可減少次數**是否大於所有 nums[i] 即可。  

時間複雜度 O(N + Q)。  
空間複雜度 O(N)。  

```python
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * (N+5)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1

        ps = 0
        for i in range(N):
            ps += diff[i]
            if nums[i] > ps:
                return False

        return True
        # return all(x<=y for x, y in zip(nums, accumulate(diff)))
```
