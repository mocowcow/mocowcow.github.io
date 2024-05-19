---
layout      : single
title       : LeetCode 3152. Special Array II
tags        : LeetCode Medium Array Simulation
---
周賽 398。這題擊殺率還挺高的，我也貢獻了一次 WA。  

## 題目

若陣列中每一對相鄰元素都是由奇偶性不同的數組成，則稱為**特殊的**。  

輸入整數陣列 nums 和二維整數陣列 queries，其中 queries[i] = [from<sub>i</sub>, to<sub>i</sub>]。  
你必須判斷子陣列 nums[from<sub>i</sub>..to<sub>i</sub>] 是否為**特殊的**。  

回傳布林陣列 answer，其中 answer[i] 代表 nums[from<sub>i</sub>..to<sub>i</sub>] 是否特殊。  

## 解法

若某個陣列是特殊的，其所有**子陣列**肯定也是特殊的。  

先找出所有最長的特殊陣列，並將同組的元素分組編號。  
只要查詢的起點和終點元素編號相同，則代表其屬於同一個特殊陣列。  

時間複雜度 O(N + Q)，其中 Q = len(queries)。  
空間複雜度 O(N)。  

```python
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        group = [0] * N
        gid = 0
        i = 0
        while i < N:
            j = i
            while j + 1 < N and nums[j] % 2 != nums[j + 1] % 2:
                j += 1
                
            # mark id 
            for idx in range(i, j + 1):
                group[idx] = gid
                
            # next group
            gid += 1
            i = j + 1
            
        return [group[s] == group[e] for s, e in queries]
```
