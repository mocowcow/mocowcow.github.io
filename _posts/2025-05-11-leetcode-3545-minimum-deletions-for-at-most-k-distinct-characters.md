---
layout      : single
title       : LeetCode 3545. Minimum Deletions for At Most K Distinct Characters
tags        : LeetCode Easy Sorting Greedy
---
weekly contest 449。

## 題目

<https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/>

## 解法

統計各元素出現次數。  
如果超過 k 種，則從出現次數最多的開始刪。  

時間複雜度 O(N + (D log D))，其中 D = 不同的元素個數。  
空間複雜度 O(N + D)。  

```python
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        a = Counter(s).most_common()
        ans = 0
        while len(a) > k:
            t = a.pop()
            ans += t[1]

        return ans
```
