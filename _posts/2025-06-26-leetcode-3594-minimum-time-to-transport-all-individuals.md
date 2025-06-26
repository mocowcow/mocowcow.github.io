---
layout      : single
title       : LeetCode 3594. Minimum Time to Transport All Individuals
tags        : LeetCode Hard BitManipulation Bitmask Heap
---
weekly contest 455。

## 題目

<https://leetcode.com/problems/minimum-time-to-transport-all-individuals/description/>

## 解法

有 n 個人要划船過河，船只有一艘且一次最多裝 k 個人。若還有人沒過，需要有 1 人從對岸把船開回來。  
每次過河的時間按照船上的人的最低速度乘上流速倍率 mul。  

---

看到 n <= 12，直覺想到 bitmask 表示剩餘人口。  
過河人口與其最大值也可以用 bitmask 優化。  

本以為是狀壓 dp，但是人可以來回過河，剩餘人口會出現**循環**。河流狀態也是循環，無法轉換成更小的子問題，故不適用 dp。  

---

已知的狀態有：剩餘人口、船的位置、流速倍率。分別以 ppl, dir, speed 表示。  

在三個狀態相同時，應避免重複計算，又要求最小時間。  
時間只增不減，可用 dijkstra 最短路，將三個狀態合併看成一個點。  

剩下就是分類討論：  

- 船在出發點，從剩餘人口枚舉不超過 k 個人過河  
- 船在終點，從抵達以口枚舉正好 1 個人把船開回去  

複雜度不會算。  

```python
class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        FULL = (1 << n) - 1

        mask_time = [0] * (1 << n)
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    mask_time[mask] = max(mask_time[mask], time[i])

        dist = [[[inf]*m for _ in range(2)] for _ in range(1 << n)]
        h = []
        heappush(h, [0, FULL, 0, 0])  # cost, ppl, dir=0/1, mul_state
        dist[FULL][0][0] = 0
        while h:
            cost, ppl, dir, mul_state = heappop(h)
            if cost > dist[ppl][dir][mul_state]:
                continue

            if dir == 0:  # at start
                for mask in range(1, 1 << n):
                    if mask.bit_count() <= k and mask | ppl == ppl:  # at most k ppl
                        d = mask_time[mask]*mul[mul_state]
                        new_cost = cost + d
                        new_ppl = ppl ^ mask
                        new_mul_state = (mul_state+floor(d)) % m
                        if new_cost < dist[new_ppl][1][new_mul_state]:
                            dist[new_ppl][1][new_mul_state] = new_cost
                            heappush(h, [new_cost, new_ppl, 1, new_mul_state])
            else:  # at end
                if ppl == 0:  # all arrived
                    return cost
                for i in range(n):
                    mask = 1 << i
                    if mask & ppl == 0:
                        d = mask_time[mask]*mul[mul_state]
                        new_cost = cost + d
                        new_ppl = ppl ^ mask
                        new_mul_state = (mul_state+floor(d)) % m
                        if new_cost < dist[new_ppl][0][new_mul_state]:
                            dist[new_ppl][0][new_mul_state] = new_cost
                            heappush(h, [new_cost, new_ppl, 0, new_mul_state])

        return -1
```
