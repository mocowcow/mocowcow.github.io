---
layout      : single
title       : LeetCode 2017. Grid Game
tags 		: LeetCode Medium PrefixSum
---
隨機抽題遇到前綴和機率有點高啊。

# 題目
輸入一個2*N矩陣，每格代表可獲得的分數，且只能獲得一次。  
有兩個機器人，每次移動只能向下或向右走。  
機器人1會選擇將機器人2的得分最小化，而機器人2會選擇最大化分數的路線。  
假設雙方都進行最佳解，求機器人2最多能拿幾分。

# 解法
機器人1只有三種路線：
1.  走到底後往下
2.  往下後走到底
3.  先走一段後往下再走到底

路線會將矩陣切成右上及左下區塊，機器人2只能擇一撿剩的。  
先做前綴和求區間值，對於每個i點，機器人2會選較大值的區塊，再拿去更新最小值。

```python
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        psum1 = [0]*(N+1)
        psum2 = [0]*(N+1)

        for i in range(1, N+1):
            psum1[i] = psum1[i-1]+grid[0][i-1]
            psum2[i] = psum2[i-1]+grid[1][i-1]

        ans = math.inf
        for i in range(N):
            robot2 = max(psum1[-1]-psum1[i+1], psum2[i])
            ans = min(ans, robot2)

        return ans
```

優化成O(1)空間解法。top為右上區塊，bottom為左下區塊。

```python
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bottom = 0
        ans = math.inf
        for i in range(len(grid[0])):
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]

        return ans
```
