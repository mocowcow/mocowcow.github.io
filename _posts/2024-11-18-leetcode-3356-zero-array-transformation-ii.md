---
layout      : single
title       : LeetCode 3356. Zero Array Transformation II
tags        : LeetCode Medium PrefixSum BinarySearch
---
weekly contest 424。  

## 題目

輸入長度 n 的整數陣列 nums，還有二維陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>, val<sub>i</sub>]。  

對於每個 queries[i]：  

- 對於 nums 在 [l<sub>i</sub>, r<sub>i</sub>] 之間的索引**至多**減少 val<sub>i</sub>。  
- 同一個查詢中，對於不同索引的減少量都是**獨立的**，不必相同。  

一個陣列的所有元素都等於 0，稱做**零陣列**。  

若執行所有操作後能使得 nums 變成**零陣列**，則回傳 true，否則回傳 false。  

在執行前 k 個查詢後，能使得 nums 變成**零陣列**，求 k 的**最小值**。  
若無法使 nums 變成**零陣列**，則回傳 -1。  

## 解法

與 Q2 差別在於每個查詢的**減少量**從 1 變成 [1, val]。差分陣列同樣可以滿足，無所謂。  

---

假設 k 個查詢可以滿足答案，則大於 k 的查詢數必定也合法；若 k 不合法，小於 k 必定也不合法。  
答案具有**單調性**，可以二分答案。  

將 Q2 的答案封裝成，做為二分時的判斷邏輯即可。  

注意：在 nums 全為 0 時，原本就是零陣列，不需任何查詢。因此下界為 1。  
注意 2：執行所有查詢後，可能也無法變成零陣列，因此二分結束後還要檢查答案一次。  

時間複雜度 O((N + Q) log Q)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        Q = len(queries)
        
        def ok(k):
            diff = [0] * (N+5)
            for l, r, val in queries[:k]:
                diff[l] += val
                diff[r+1] -= val

            ps = 0
            for i in range(N):
                ps += diff[i]
                if nums[i] > ps:
                    return False
            return True

        lo = 0
        hi = Q
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid

        if not ok(lo):
            return -1

        return lo
```
