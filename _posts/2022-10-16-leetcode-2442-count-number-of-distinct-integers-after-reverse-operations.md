--- 
layout      : single
title       : LeetCode 2442. Count Number of Distinct Integers After Reverse Operations
tags        : LeetCode Easy Array HashTable
---
周賽315。有點鳥的題，可能是昨晚雙周賽太難，今天放水。  

# 題目
輸入由正整數組成的陣列nums。  
你必須取出陣列中每個整數，將其數字反轉後加回陣列的的末端。此操作只應該針對nums中原有的整數。  

回傳處理後的陣列中有多少**不同**的整數。  

# 解法
如果直接將反轉後的新整數加回nums中不太好處理，不如開新的集合，把所有整數n和反轉後的整數r加入去重，最後回傳集合大小。  

時空間複雜度O(N)。  

```python
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen=set(nums)
        
        for n in nums:
            s=str(n)[::-1]
            r=int(s)
            seen.add(r)
            
        return len(seen)
```
