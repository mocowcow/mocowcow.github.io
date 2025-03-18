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

---

來算算究竟有多少計算量。  

R 轉成十進制的最大位數 N = 9。  
乘積的不同個數有 P 個。  
總和的不同個數有 S 個。  
每個狀態需要枚舉 D = 10 種數字，轉移 D 次。  

S 上限很明顯是 N \* 9 = 81。  
先算不包含 P 的部分，O(N \* S \* D) =  = 9 \* 81 \* 10 = 7290。  

那麼 P 呢？  
似乎沒有什麼公式可以算，但可以寫一小段程式暴力算看看到底有幾種：  

```python
s = {1}
for _ in range(9):
    s2 = set()
    for x in s:
        for y in range(10):
            s2.add(x * y)
    s = s2
print(len(s))  # 3026
```

乍看之下很可怕，其實只有 3026 種。  
不過 7290 \* 3026 還是高達 2e2，好像還是很可怕。  
但是 P 和 S 有特定的對應關係，並非任意搭配，所以實際上也不會這麼多。  
總之這題最難的點是**說服自己相信複雜度**。  

時間複雜度 O(N \* P \* S \* D)。  
空間複雜度 O(N \* P \* S)。

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
