---
layout      : single
title       : LeetCode 3587. Minimum Adjacent Swaps to Alternate Parity
tags        : LeetCode Medium Greedy
---
biweekly contest 159。  
近幾次最難搞的 Q1。  

## 題目

<https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/description/>

## 解法

交換相鄰元素，使得每對相鄰的元素**奇偶性**不同。  
最終情況只有兩種：  

- 奇, 偶, 奇, 偶,..  
- 偶, 奇, 偶, 奇,..  

枚舉兩種情況即可。  

---

假設我們要將所有偶數元素填入偶數索引。  
維護偶數元素的出現位置，記做 even。  
排序後，依序填入 target = 0, 2, 4.. 即可。每次填入需移動次數為 even[i] 與 target 的絕對差。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        odd = []
        even = []
        for i, x in enumerate(nums):
            if x % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        def f(a):
            # put a[i] into even indexes
            sz = (N+1) // 2
            if len(a) != sz:  # invalid
                return inf
            res = 0
            for i, src in enumerate(a):
                target = i*2
                res += abs(target-src)
            return res

        ans = min(f(odd), f(even))

        if ans == inf:
            return -1

        return ans
```
