---
layout      : single
title       : LeetCode 3443. Maximum Manhattan Distance After K Changes
tags        : LeetCode Medium Greedy
---
weekly contest 435。

## 題目

<https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description/>

## 解法

曼哈頓距離是兩軸絕對差的和，兩軸互不影響，可以分開討論。  

假設只有 N, S 兩種方向：  
> SNN  
> 往下走 1 次，又往上走 2 次  

其中 S 和 N 抵銷 1 次，所以等於往上走 1 次。  
如果把 S 修改成 N，會變成 NNN，等於往上走 3 次。  
每**修改**一次反方向，能夠使**距離增加 2**。  

---

統計 N, S 出現次數，修改前的距離為 abs(N - S)；可修改次數為 min(N, S)。  

W, E 同理，求出兩軸距離和 dist 還有可修改次數 change  
修改次數受限於 k，所以實際最遠距離為 dist + min(change, k) * 2。  

---

但是題目求的是**任意時間點**的最大值，而不是最後才修改。  
在遍歷 s 統計個方向次數時，就要及時更新答案。例如：  
> s = "SSNN", k = 1  
> 在第一次碰到 N 的時候修改成 S  
> "SSS" 才是最佳答案  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        N = S = W = E = 0
        ans = 0
        for c in s:
            if c == "N":
                N += 1
            elif c == "S":
                S += 1
            elif c == "E":
                E += 1
            else:
                W += 1

            dist = abs(N - S) + abs(W - E)
            change = min(N, S) + min(W, E)
            ans = max(ans,  dist + min(change, k) * 2)

        return ans
```

其實根本不用在意可以修改幾次，只要保證修改後**不超過當前字元數**即可。  

```python
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x = y = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1

            dist = min(abs(x) + abs(y) + k * 2, i + 1)
            ans = max(ans, dist)

        return ans
```

也有人直接枚舉四個方位。  
往指定方位移動的話距離加 1；否則距離減 1，可翻轉次數加 1。並在遍歷途中更新答案。  

```python
class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        def f(dirs):
            dist = 0
            change = 0
            mx = 0
            for c in s:
                if c in dirs:
                    dist += 1
                else:
                    dist -= 1
                    change += 1
                mx = max(mx, dist + min(change, k) * 2)
            return mx

        return max(
            f("NE"),
            f("ES"),
            f("SW"),
            f("WN")
        )
```
