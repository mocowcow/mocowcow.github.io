---
layout      : single
title       : LeetCode 3283. Maximum Number of Moves to Kill All Pawns
tags        : LeetCode Hard BitManipulation Bitmask DP BFS
---
weekly contest 414。  

## 題目

有個 50 x 50 的棋盤，上方有一個**馬**和一些**兵**。  
輸入兩個整數 kx, ky，其中 (kx, ky) 代表馬的位置。  
還有二維整數陣列 positions，其中 positions[i] = [x<sub>i</sub>, y<sub>i</sub>] 代表兵的位置。  

Alice 和 Bob 在玩一種回合制遊戲，由 Alice 先。每回合：  

- 玩家控制馬，並吃掉還存在棋盤上的任意一個兵，且**不能繞遠路**。  
    注意：可以選擇**任何**兵，不一定要選距離馬最近的兵。  
- 馬在移動的過程，**可能**會碰到其他兵，但他們**不會被吃掉**。在本回合內只有被選中的兵會被吃。  

Alice 希望使得兩人的**總移動次數最大化**，而 Bob 則希望**最小化**。  

求兩者都選擇**最佳策略**的情況下，Alice 可以達到的**最大總移動次數**。  

注意：馬有 8 種移動方向，都是朝某個方向前進 1 格，然後再朝垂直的方向前進 1 格。  

## 解法

這個馬的移動方式很麻煩，好像沒什麼公式算，只能用 bfs 暴力模擬，枚舉出發點、求出各座標所需的移動次數。  

棋盤大小寬度 L = 50，每次 bfs 複雜度 O(L^2)。  
有 L^2 個起點，總複雜度 O(L^4)，大約 6e6 計算量，能不能過還真不好說。  

但是棋盤中最多只會有 N = 15 個兵。  
雖然是要由某個位置 (px, py) 走到某個兵 (x, y) 上，但**反過來走**也是等價的。  
如此一來最多只需要 15 次 bfs，大概 3e4 計算量，看起來可行不少。  

以 dist[i][px][py] 表示 positions[i] 與 (px, py) 的最短距離。  

---

接下來的問題是，要**選擇哪個**兵吃？  

就算兩者吃的順序不同，也可能會剩餘相同的兵存活，有**重疊的子問題**，因此考慮 dp。  
而每個兵只能被選一次，最多也只有 15 個，可以用 bitmask 表示存活狀態，做**狀態壓縮 dp**。  

此外，我們還需要維護**當前位置**。  
當前位置只可能是起點 (kx, ky) 或是某個兵的位置，因此直接以狀態 i 表示出發點為 positions[i]。  
至於起點 (kx, ky) 則直接加入 positions 中，即 positions[N]。  

最後，因為兩人策略不同，轉移時分別用 max/min。  
再多一個狀態 is_alice = 0/1，其中 1 代表是 Alice 的回合，要採用 max；否則採用 min。  

---

定義 dp(i, mask)：當前位於 positions[i]，且還有 mask 個兵可以選。  
轉移：dp(i, mask) = max(dp(j, new_mask) + dist[j][px][py])。  
base：當 mask = (1 << N) - 1 時，全部兵都吃完，回傳 0。  

時間複雜度 O(N \* L^2 + N^2 \* 2^N)。  
空間複雜度 O(N \* L^2 + N \* 2^N)。  

最初從 positions[N] = (kx, ky) 出發、所有兵都可選，mask = 0、且由 Alice 先手，is_alice = 1。  
答案入口為 dp(N, 0, 1)。  

```python
DIRS = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
L = 50

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        N = len(positions)
        positions.append([kx, ky])
        dist = [[[-1] * L for _ in range(L)] for _ in range(N)]

        def bfs(i):
            px, py = positions[i]
            q = [[px, py]]
            dist[i][px][py] = 0
            step = 1
            while q:
                q2 = []
                for x, y in q:
                    for dx, dy in DIRS:
                        xx, yy = x + dx, y + dy
                        if xx < 0 or xx >= L or yy < 0 or yy >= L or dist[i][xx][yy] != -1:
                            continue
                        q2.append([xx, yy])
                        dist[i][xx][yy] = step
                q = q2
                step += 1
            return

        for i in range(N):
            bfs(i)

        @cache
        def dp(i, mask, is_alice):
            if mask == (1 << N) - 1:
                return 0
            px, py = positions[i]
            compare = max if is_alice else min  # max for alice, min for bob
            res = -inf if is_alice else inf
            for j in range(N):
                if mask & (1 << j) != 0:
                    continue
                new_mask = mask | (1 << j)
                res = compare(
                    res, dp(j, new_mask, is_alice ^ 1) + dist[j][px][py])
            return res

        return dp(N, 0, 1)
```

先預處理所有移動距離，複雜度 O(L^4)。  
只稍微快了一點點。  

時間複雜度 O(N^2 \* 2^N)，預處理不計入。  
空間複雜度 O(N \* 2^N)，預處理不計入。  

```python
DIRS = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
L = 50
dist = [[[[-1] * L for _ in range(L)] for _ in range(L)] for _ in range(L)]


def bfs(px, py):
    q = [[px, py]]
    dist[px][py][px][py] = 0
    step = 1
    while q:
        q2 = []
        for x, y in q:
            for dx, dy in DIRS:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx >= L or yy < 0 or yy >= L or dist[px][py][xx][yy] != -1:
                    continue
                q2.append([xx, yy])
                dist[px][py][xx][yy] = step
        q = q2
        step += 1
    return


for px in range(L):
    for py in range(L):
        bfs(px, py)


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        N = len(positions)
        positions.append([kx, ky])

        @ cache
        def dp(i, mask, is_alice):
            if mask == (1 << N) - 1:
                return 0
            px, py = positions[i]
            compare = max if is_alice else min  # max for alice, min for bob
            res = -inf if is_alice else inf
            for j in range(N):
                if mask & (1 << j) != 0:
                    continue
                x, y = positions[j]
                new_mask = mask | (1 << j)
                res = compare(
                    res, dp(j, new_mask, is_alice ^ 1) + dist[x][y][px][py])
            return res

        return dp(N, 0, 1)
```
