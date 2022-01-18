---
layout      : single
title       : LeetCode 1345. Jump Game IV"
tags 		: LeetCode Hard BFS
---
本想說很單純的題目，結果被騙了一次TLE。

# 題目
輸入長度為N的整數陣列arr，求從arr[0]需幾步可到達arr[N-1]。  
每步可以從i移動到i+1、i-1或任何和arr[i]同數值的位置。

# 解法
先依數值將索引塞入dict，從0開始做BFS，每次檢查前後位及同值的其他索引位置，並清空已加入的dict。

```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        goal = len(arr)-1
        tunnel = defaultdict(list)
        for i, val in enumerate(arr):
            tunnel[val].append(i)

        visited = set()
        step = 0
        q = [0]
        while q:
            t = []
            for i in q:
                if i == goal:
                    return step
                visited.add(i)
                for x in tunnel[arr[i]]:
                    if x not in visited:
                        t.append(x)
                tunnel[arr[i]].clear()  # 避免TLE
                for x in (i+1, i-1):
                    if 0 <= x <= goal and x not in visited:
                        t.append(x)
            q = t
            step += 1
```
