---
layout      : single
title       : LeetCode 3080. Mark Elements on Array by Performing Queries
tags        : LeetCode Medium Array Heap
---
雙周賽 126。

## 題目

輸入長度 n 的正整數陣列 nums。  

另外輸入長度 m 二維整數陣列 queries，其中 queries[i] = [index<sub>i</sub>, k<sub>i</sub>]。  

最初，nums 中的所有元素都是**未標記**的。  
你必須**依序**執行 m 次查詢，每次查詢你必須：  

- 若 index<sub>i</sub> 未標記，則將其標記  
- 從未標記的元素中，選擇 k<sub>i</sub> 個**最小值**標記。若存在多個最小值，則選擇**索引較小**的。若剩餘不足 k<sub>i</sub> 個，則全部標記  

回傳長度 m 陣列 answer，其中 answer[i] 代表第 i 次查詢後，未標記的元素**總和**。  

## 解法

看到取最小值，就想到用 min heap 了。  
以 [value, index] 為鍵值，將所有元素裝進 heap。同時維護一個 vis 陣列表示元素是否標記過。  

題目要求的是**未標記的總和**，所以要先算出原本的總和，每標記一次就從中扣除。  
對於每次查詢，先檢查指定的標記位置，然後取 k 個最小值標記。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)，答案空間不計入。  

```python
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        h = []
        for i, x in enumerate(nums):
            heappush(h, [x, i])
            
        sm = sum(nums)
        vis = [False] * N
        ans = []
        for qi, k in queries:
            if not vis[qi]:
                vis[qi] = True
                sm -= nums[qi]
            
            while h and k:
                v, i = heappop(h)
                if not vis[i]:
                    vis[i] = True
                    k -= 1
                    sm -= v
                    
            ans.append(sm)
            
        return ans
```
