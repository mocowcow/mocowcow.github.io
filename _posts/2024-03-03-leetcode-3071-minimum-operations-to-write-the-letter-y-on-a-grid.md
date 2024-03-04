---
layout      : single
title       : LeetCode 3071. Minimum Operations to Write the Letter Y on a Grid
tags        : LeetCode Medium Array Matrix Simulation Greedy
---
周賽387。

## 題目

輸入 n\*n 的網格 grid，保證 n 是奇數，且 grid[r][c] 只會是 0, 1 或 2。  

如果某個格子滿足以下條件之一，則稱其在 Y 字形上：  

- 位於 grid 左上角格子往中央格子的對角線上  
- 位於 grid 右上角格子往中央格子的對角線上  
- 位於中央格子往最底部的垂直線上  

若滿足以下所有條件，則認為 Y 字形存在於此網格上：  

- 在 Y 字形上的格子，其值都相同  
- 不在 Y 字形上的格子，其值都相同  
- 在 Y 字形上的格子與不在 Y 字形上的格子，兩者值不同  

求**最少**需要幾次操作，才能使得 Y 字形存在於此網格上。  

## 解法

網格上只能有 2 種數字。  
而數字只有 3 種，總共只有 6 種方案。  

直接枚舉所有方案，模擬弄出 Y 字型需要需要修改多少次，並以次數更新答案最小值。  
判斷是否屬於 Y 字上比較囉嗦，建議提取成函數，看起來容易理解。  

時間複雜度 O(N^2)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        N = len(grid)
        mid = N // 2
        
        def is_y(r, c):
            if r < mid:
                return c in [r, N-1-r]
            else:
                return c == mid
        
        def f(x, y):
            cnt = 0
            for r in range(N):
                for c in range(N):
                    if is_y(r, c):
                        if grid[r][c] != y:
                            cnt += 1
                    else:
                        if grid[r][c] != x:
                            cnt += 1
            return cnt
        
        ans = inf
        for x in range(3):
            for y in range(3):
                if x != y:
                    ans = min(ans, f(x, y))
                    
        return ans
```

如果格子上的值有很多種，那就不能暴力枚舉了。  

為了使操作次數最小化，在 Y 字型上選擇**出現頻率最高**的值更合適。非 Y 字上也同理。  
分別統計兩區域中，各值的出現頻率。  

設 Y 字上出現頻率最高的值為 i，頻率為 cnt_y[i]，而非 Y 字上為 j，頻率為 cnt_not_y[j]。  
則所需修改次數為 N^2 - cnt_y[i] - cnt_not_y[j]。  

但 i, j 不可為相同值，因此要分別找到出現頻率最高的兩個值，設為 i1, i2 和 j1, j2。  
若 i1 等於 j1，則答案必是 (i1, j2), (i2, j1) 兩者之一所組成。  

時間複雜度 O(N^2)。  
空間複雜度 O(k log k)，其中 k 為 gridr[r][c] 可能的值。若直接遍歷找最大值可降低至 O(k)。  

```python
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        N = len(grid)
        mid = N // 2
        
        def is_y(r, c):
            if r < mid:
                return c in [r, N-1-r]
            else:
                return c == mid
        
        cnt_y = [0] * 3 # all possible values
        cnt_not_y = [0] * 3
        for r in range(N):
            for c in range(N):
                x = grid[r][c]
                if is_y(r,c):
                    cnt_y[x] += 1
                else:
                    cnt_not_y[x] += 1
                    
        def get_first_second(cnt):
            a = list(range(3)) # enumerate all possible values
            a.sort(key=lambda x:-cnt[x]) # decreasing sort by freq
            return a[:2]
            
        i1, i2 = get_first_second(cnt_y)
        j1, j2 = get_first_second(cnt_not_y)

        if i1 != j1:
            return N*N - (cnt_y[i1] + cnt_not_y[j1])
        else:
            return N*N - max(
                cnt_y[i1] + cnt_not_y[j2],
                cnt_y[i2] + cnt_not_y[j1]
            )
```
