---
layout      : single
title       : LeetCode 3091. Apply Operations to Make Sum of Array Greater Than or Equal to k
tags        : LeetCode Medium Array Greedy BinarySearch
---
周賽 390。寫這題腦子進水了，竟然錯兩次，上分機會又飛走。  

## 題目

輸入正整數 k。最初你擁有陣列 nums = [1]。  

你可以執行以下操作任意次(包含零次)：  

- 選擇 nums 中的任意元素，並將其加 1  
- 複製 nums 中的任意元素，並加到 nums 的最末端  

求**最少**需要幾次操作，才能使得 nums 的總和大於等於 k。  

## 解法

實質有效操作分成兩種：  

- 對最大元素加 1，稱作 add  
- 複製最大元素，稱作 dup  

複製的元素越大越好，因此最佳方案是對**同個數**進行所有 add 操作，然後才 dup。  
那 add 和 dup 要各幾次？  

---

先講講比賽時不小心走的彎路。  

如果 x 次操作可以滿足 k，則 x + 1 也必定滿足；反之，x 次不滿足，則 x - 1 必定不滿足。  
答案具有單調性，可以二分。  

要判斷 x 次操作能否滿足，只要枚舉 add 的次數 0\~x，而 dup 的次數就是 x - add。  
每次判斷需要 O(N)，共需要 O(log N) 次。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minOperations(self, k: int) -> int:
        
        def ok(x):
            for add in range(x + 1):
                base = 1 + add
                dup = x - add + 1
                if base * dup >= k:
                    return True
            return False
        
        lo = 0
        hi = k
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid
                
        return lo
```
