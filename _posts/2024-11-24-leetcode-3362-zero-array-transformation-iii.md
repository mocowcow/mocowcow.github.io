---
layout      : single
title       : LeetCode 3362. Zero Array Transformation III
tags        : LeetCode Medium PrefixSum Sorting Greedy SegmentTree Heap
---
biweekly contest 144。  
這屌題也是 5 分，其實應該給個 6 分。  

## 題目

輸入長度 n 的整數陣列 nums，還有二維陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>]。  

對於每個 queries[i]：  

- 對於 nums 在 [l<sub>i</sub>, r<sub>i</sub>] 之間的索引**至多**減少 1。  
- 同一個查詢中，對於不同索引的減少量都是**獨立的**，不必相同。  

一個陣列的所有元素都等於 0，稱做**零陣列**。  

若執行所有操作後能使得 nums 變成**零陣列**，則回傳 true，否則回傳 false。  

求**最多**可從 queries 移除多少元素，並且依然使得 nums 成為**零陣列**。  
若不可能成為**零陣列**則回傳 -1。  

## 解法

有打上次周賽的同學應該很熟悉，這題應該可以用**差分**做。  

---

區間**刪除盡可能多**，等價於**保留盡可能少**。  

由左至右、循序考慮每個 nums[i]，在覆蓋區間不足時嘗試加入新區間。  
怎麼決定選誰？試想以下例子：  

> 當前 nums[5] = 1，但 ps[i] = 0 的區間數不足  
> 有 [2,5], [2,7], [4,8] 三個區間可選，選哪個最佳？  

因為我們是**由左至右**處理，所以 num[0..4] 肯定已經被滿足，不需要考慮。  
而 [4,8] 可以對 [5..8] 三個位置做出貢獻，因此選擇 [4,8] 是最佳方案。  

---

另外還需要**維護可選的區間**，並取出**右端點最大者**，可使用 max heap。  
注意：在 ps[i] 不足時，heap 裝的區間有可能位於 i 左方，無法使用。  

時間複雜度 O(N + Q log Q)。  
空間複雜度 O(N + Q)。  

```python
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        diff = [0] * (N+5)
        ps = 0

        q = deque(sorted(queries))
        h = [] # right bound of available invervals
        ans = len(queries)
        for i in range(N):
            # maintain available intervals
            while q and q[0][0] == i:
                t = q.popleft()
                heappush(h, -t[1])


            ps += diff[i]
            # add new intervals while not enough
            while ps < nums[i] and h:
                e = -heappop(h)
                if e >= i: # [i, r] increased by 1
                    ans -= 1
                    ps += 1
                    diff[e+1] -= 1
            
            # still not possible to zero
            if ps < nums[i]:
                return -1

        return ans
```
