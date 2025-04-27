---
layout      : single
title       : LeetCode 3529. Count Cells in Overlapping Horizontal and Vertical Substrings
tags        : LeetCode Medium String PrefixSum
---
biweekly contest 155。  
這題給中等是真的很變態，難度分級僅供參考。  
但我一次就寫對，給自己一個肯定。  

## 題目

<https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/>

## 解法

水平、垂直是其實是兩個相同的子問題：  
> 在拼接起來的字串中找 pattern，並標記屬於 pattern 的格子。  

將子問題封裝成函數 solve() 以便重複使用。  

---

找子字串很簡單，套個 KMP 或是 rolling hash 就可以 O(N) 解決。  

接下來是標記 pattern 所屬的格子。  
那如果字串是 "aaaa..." 模式串是 "aa.."，會找到好幾個重複的 pattern。  
暴力標記複雜度會上升到平方級別，需要更有效率的方式。  

維護**差分陣列** diff，對每個 pattern 所屬區間 [i..i+P-1] 加 1。  
對 diff 做前綴和 ps，只要某格子的 ps > 0 代表有被覆蓋，將該格子標記。  

至於怎麼知道串接字串每個格子對應到哪個 grid[i][j]？  
最簡單的方式是在串接的過程中直接順便維護原始座標陣列 cells[idx] = (i, j)，這樣可以直接查表。  

---

先串接水平字串，代入 solve() 求標記格子。  
再串接垂直字串，代入 solve() 求標記格子。  
答案為兩者被標記格子的交集數。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        M, N = len(grid), len(grid[0])
        P = len(pattern)
        SZ = M * N

        def solve(chars, mp):
            s = "".join(chars)
            diff = [0] * (SZ + 1)
            for idx in KMP_all(s, pattern):
                diff[idx] += 1
                diff[idx + P] -= 1

            ps = 0
            marked = set()
            for i in range(SZ):
                ps += diff[i]
                if ps > 0:
                    marked.add(mp[i])
            return marked

        # horizontal
        h_chars = []
        h_mp = []
        for r in range(M):
            for c in range(N):
                h_chars.append(grid[r][c])
                h_mp.append(r * N + c)

        # vertical
        v_chars = []
        v_mp = []
        for c in range(N):
            for r in range(M):
                v_chars.append(grid[r][c])
                v_mp.append(r * N + c)

        h_marked = solve(h_chars, h_mp)
        v_marked = solve(v_chars, v_mp)
        ans = h_marked & v_marked  # both marked in horizontal and verital

        return len(ans)


# PMT optimized version
def prefix_function(s):
    N = len(s)
    pmt = [0] * N
    for i in range(1, N):
        j = pmt[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pmt[j - 1]
        if s[i] == s[j]:
            j += 1
        pmt[i] = j
    return pmt


# search p in s, return every starting idnex of p
def KMP_all(s, p):
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i - j + 1)
            j = pmt[j - 1]
    return res
````
