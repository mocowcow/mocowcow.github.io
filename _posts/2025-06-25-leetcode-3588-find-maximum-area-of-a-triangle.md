---
layout      : single
title       : LeetCode 3588. Find Maximum Area of a Triangle
tags        : LeetCode Medium Greedy
---
biweekly contest 159。  
個人感覺比 Q1 好搞一些。  

## 題目

<https://leetcode.com/problems/find-maximum-area-of-a-triangle/description/>

## 解法

求至少有一條邊與 x 軸或 y 軸平行的三角型**最大**面積的**兩倍**。  
分類討論兩種情況：  

- 與 x 軸平行，有兩點共享 y 軸  
- 與 y 軸平行，有兩點共享 x 軸  

---

枚舉 y 軸，選擇最距離遠的兩點構成與 x 軸平行的邊。  
第三點應距離 y 越遠越好，應選擇所有點中 y 值最大或最小者，計算面積更新答案。  

與 x 軸平行同理。  

注意：當 y 的最大 / 最小值等於 y 時，面積面積會等於 0。因此答案初始不可設為 -1。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        x_mp = defaultdict(list)
        y_mp = defaultdict(list)

        for x, y in coords:
            x_mp[x].append(y)
            y_mp[y].append(x)

        def f(mp):
            res = 0
            mn = min(mp)
            mx = max(mp)
            for x, vals in mp.items():
                if len(vals) > 1:
                    vals.sort()
                    width = vals[-1] - vals[0]
                    height = max(x - mn, mx - x)
                    res = max(res, width * height)
            return res

        ans = max(f(x_mp), f(y_mp))
        if ans == 0:
            return -1

        return ans
```
