---
layout      : single
title       : LeetCode 2139. Minimum Moves to Reach Target Score
tags 		: LeetCode Medium Math Greedy
---
模擬周賽276。也是很直覺的題目。

# 題目
輸入整數target代表目標及maxDoubles代表可翻倍次數。玩一種遊戲，每次從n=1開始，求最少幾次行動後n=target。  
你有兩種行動：  
1. n=n+1
2. n=n*2，但一場遊戲中最多只能使用maxDoubles次

# 解法
遊戲玩多了都知道加倍這種東西越晚用越強。  
逆向思考，n從target開始往回推，就能達到最小行動次數。維護ans表示行動數，如果target是奇數只好先-1，ans+1。  
再還有翻倍次數時，若偶數n就砍半，否則乖乖n-1，記得ans+1。等到次數用完後，(n-1)就是還需要慢慢-1的次數，加上ans就是答案。

```python
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = target
        ans = 0
        if n & 1:
            n -= 1
            ans += 1

        while n > 1 and maxDoubles > 0:
            if not n & 1:
                n //= 2
                maxDoubles -= 1
            else:
                n -= 1
            ans += 1

        return ans+n-1

```
