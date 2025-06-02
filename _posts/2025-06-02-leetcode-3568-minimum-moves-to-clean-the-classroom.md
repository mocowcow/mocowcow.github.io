---
layout      : single
title       : LeetCode 3568. Minimum Moves to Clean the Classroom
tags        : LeetCode Medium BFS BitManipulation Bitmask
---
weekly contest 452。  
又又是複雜度妙妙屋。  

## 題目

<https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/description/>

## 解法

簡單來說就是從 "S" 出發，求所有的垃圾點 "L" 都走過至少一次的最小步數。  
注意到垃圾最多 10 個，可用 bitmask 表示垃圾是否收過的狀態。  
如果只有這樣就是普通的 bfs。  

---

但是有體力值的限制，體力剩 0 就無法移動。  
所以不能直直往垃圾走，有時候需要繞到 "R" 補充體力。  

所以 bfs 的狀態需要再加上當前體力 e。  
狀態為 (r, c, e, mask)，共有 N^2 \* 2^L \* E 個狀態。  

---

先遍歷一次找起點和垃圾位置。  
然後按照上述狀態做 bfs，按照各格子效果調整體力即可。  

但不知道是卡常數，或是因為非期望解法，需要充分優化才不會超時。  
優化 1：把最大的 2^L 擺在最內層，減少記憶體分配次數。  
優化 2：枚舉方向直接寫死，避免使用 pairwise 函數成本。  

時間複雜度 O(MN \* energy \* 2^L)，其中 L = 垃圾數。  
空間複雜度 O(MN \* energy \* 2^L)。  

```python
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        a = classroom
        M, N = len(a), len(a[0])

        x = y = 0
        trash = []
        for r in range(M):
            for c in range(N):
                if a[r][c] == "L":
                    trash.append((r, c))
                elif a[r][c] == "S":
                    x, y = r, c

        if not trash:
            return 0

        L = len(trash)
        FULL = (1 << L) - 1
        trash_mask = [[0] * N for _ in range(M)]
        for i, (r, c) in enumerate(trash):
            trash_mask[r][c] = 1 << i

        # 20 * 20 * 50 * 2^10
        vis = [[[[False] * (FULL + 1) for _ in range(energy + 1)]
                for _ in range(N)] for _ in range(M)]

        q = deque()
        q.append([x, y, energy, 0])
        vis[x][y][energy][0] = True
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == FULL:
                    return step

                if e == 0:
                    continue

                for dx, dy in DIRS:
                    rr, cc = r + dx, c + dy
                    if 0 <= rr < M and 0 <= cc < N and a[rr][cc] != "X":
                        new_e = energy if a[rr][cc] == "R" else e - 1
                        new_mask = (
                            mask if a[rr][cc] != "L" else mask | trash_mask[rr][cc]
                        )
                        if not vis[rr][cc][new_e][new_mask]:
                            vis[rr][cc][new_e][new_mask] = True
                            q.append([rr, cc,  new_e, new_mask])
            #
            step += 1

        return -1
```

仔細想想，如果 (r, c, mask) 相同，剩餘體力應該是越大越好。  
如果能以體力 e 抵達，小於 e 的體力不可能得出更好的表現。  
可改為 vis[r][c][mask] 維護最大體力數，避免過多無效移動。  

雖然 vis 陣列減少一個維度，但應該還是有奇怪的順序能以不同體力抵達相同狀態，故空間複雜度不變。  

```python
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        a = classroom
        M, N = len(a), len(a[0])

        x = y = 0
        trash = []
        for r in range(M):
            for c in range(N):
                if a[r][c] == "L":
                    trash.append((r, c))
                elif a[r][c] == "S":
                    x, y = r, c

        if not trash:
            return 0

        L = len(trash)
        FULL = (1 << L) - 1
        trash_mask = [[0] * N for _ in range(M)]
        for i, (r, c) in enumerate(trash):
            trash_mask[r][c] = 1 << i

        dist = [[[-1] * (FULL + 1) for _ in range(N)] for _ in range(M)]

        q = deque()
        q.append([x, y, energy, 0])
        dist[x][y][0] = energy
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == FULL:
                    return step

                if e == 0:
                    continue

                for dx, dy in DIRS:
                    rr, cc = r + dx, c + dy
                    if 0 <= rr < M and 0 <= cc < N and a[rr][cc] != "X":
                        new_e = energy if a[rr][cc] == "R" else e - 1
                        new_mask = (
                            mask if a[rr][cc] != "L" else mask | trash_mask[rr][cc]
                        )
                        if new_e > dist[rr][cc][new_mask]:
                            dist[rr][cc][new_mask] = new_e
                            q.append([rr, cc, new_e, new_mask])
            #
            step += 1

        return -1
```
