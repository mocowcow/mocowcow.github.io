---
layout      : single
title       : LeetCode 3490. Count Beautiful Numbers
tags        : LeetCode Hard DP DFS
---
weekly contest 441。  
大概是最近幾次最簡單 Q4。  
我看複雜度很奇怪就沒做了，沒想到就是這樣而已。  

## 題目

<https://leetcode.com/problems/count-beautiful-numbers/description/>

## 解法

統計 [L, R] 區間內元素個數通常是**數位 dp**。  
先求 [1, R]，再扣掉 [1, L-1] 就是答案。  

---

枚舉第 i 位要填什麼數，維護乘積 prod 還有總和 sm。  
填入數字 j 時：  

- j 是第一個非零數字，prod 和 sm 初始化為 j。  
- 否則 prod *= j 然後 sm += j。  

遞迴到 i = N 時，所有數字都填完。  
若是有效數字，且 prod 可被 sm 整除，回傳 1；否則不合法，回傳 0。  

```python
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:

        def solve(num):
            s = str(num)
            N = len(s)

            @cache
            def dp(i, is_limit, is_num, prod, sm):
                if i == N:
                    return 1 if is_num and prod % sm == 0 else 0
                res = 0
                down = 0
                up = 9 if not is_limit else int(s[i])
                for j in range(down, up + 1):
                    new_limit = is_limit and j == up
                    new_is_num = is_num or (j > 0)
                    new_prod = j if not is_num else prod * j
                    new_sm = sm + j
                    res += dp(i + 1, new_limit, new_is_num, new_prod, new_sm)
                return res

            return dp(0, True, False, 1, 0)

        ans = solve(r) - solve(l-1)

        return ans
```
