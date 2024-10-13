---
layout      : single
title       : LeetCode 3320. Count The Number of Winning Sequences
tags        : LeetCode Hard DP
---
weekly contest 419。  
這題有點小陷阱，平常都是 Alice 贏，這次改 Bob 贏，騙了我一個 WA。  

## 題目

Alice 和 Bob 在玩一個 n 回合的遊戲。  
每回合他們可以各自選擇：火、水、土屬性的的怪物，克制的一方可以得分。  

- 火克制土。
- 水克制火。  
- 土克制水。  

輸入由 'F', 'W' 和 'E' 組成的字串 s，代表 Alice 每回合召喚的怪物：  

- 若 s[i] == 'F'，代表召喚火。  
- 若 s[i] == 'W'，代表召喚水。  
- 若 s[i] == 'E'，代表召喚土。  

Bob 尚未決定出招順序，但保證不會在連續兩個回合召喚相同的怪物。  
若在 n 回合後 Bob 的總分嚴格大於 Alice，則 Bob 獲勝。  

求 Bob 可以戰勝 Alice 的不同出招順序有幾種。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

只要知道 Bob 比 Alice 高分就行，實際上幾分不重要。  
因此只須要維護兩者分數差。  

Bob 的出招順序不同，也可能在相同的回合得到相同分數差。有**重疊的子問題**，考慮 dp。  

定義 dp(i, prev, score)：在第 i 回合時，兩人分數差為 score 且不能出 prev 的情況下，有幾種出招順序可以贏。  
轉移：dp(i, prev, score) = sum(dp(i+1, curr, score+delta))，其中 curr!=prev，delta 為分數變化。  
base：當 i = N 時，遊戲結束，若 score 大於 0 則回傳 1；否則為 0。  

第一回合可以隨便出，prev 填一個不屬於 FWE 的字元即可。  
答案入口 dp(0, "#", 0)。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countWinningSequences(self, s: str) -> int:
        N = len(s)

        @cache
        def dp(i, prev, score):
            if i == N:
                return int(score > 0)
            res = 0
            for curr in "FWE":
                if curr == prev:
                    continue
                delta = f(curr, s[i])
                res += dp(i+1, curr, score+delta)
            return res % MOD

        return dp(0, "#", 0)


def f(x, y):
    match x + y:
        case "FE":
            return 1
        case "EF":
            return -1
        case "WF":  
            return 1
        case "FW":
            return -1
        case "EW":
            return 1
        case "WE":
            return -1
    return 0
```
