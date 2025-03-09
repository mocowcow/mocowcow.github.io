---
layout      : single
title       : LeetCode 3477. Fruits Into Baskets II
tags        : LeetCode Easy Simulation
---
weekly contest 440。

## 題目

<https://leetcode.com/problems/fruits-into-baskets-ii/description/>

## 解法

暴力模擬。  
從左到右枚舉水果 x，然後在 basket 中找最靠左且大於等於 x 的可用籃子。  
用過的籃子改成 0 避免重複使用；找不到可用籃子則答案加 1。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for x in fruits:
            for j, y in enumerate(baskets):
                if x <= y:
                    baskets[j] = 0
                    break
            else:
                ans += 1
        
        return ans
```
