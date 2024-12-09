---
layout      : single
title       : LeetCode 3376. Minimum Time to Break Locks I
tags        : LeetCode Medium Simulation DP BitManipulation Bitmask
---
biweekly contest 145。  
這題好像有點爭議，暴力枚舉聽說會卡常數，狀壓 dp 好像不該出現在 Q2，非常尷尬。  

## 題目

Bob 被關在迷宮裡，需要破壞 n 個鎖才能出去，但是破壞鎖需要**能量**。  
輸入整數陣列 strength，其中 strength[i] 代表破壞第 i 個鎖需要的能量。  

Bob 有一把劍，特徵如下：  

- 能量初始值為 0。  
- 能量恢復速率 X 初始值為 1。  
- 每分鐘，劍的能量會增加 X。  
- 想打開第 i 個鎖，**至少**需要能量 strength[i]。  
- 每破壞一個鎖，能量都會歸零，但是 X 會增加 K。  

求打開 n 個鎖需要的**最少**時間。  

## 解法

n 上限為 8，可以直接枚舉 8! = 40320 種排列，每種排列需要 O(n) 模擬。  

若開鎖需要能量 req，則需要等待 ceil(req/x) 分鐘恢復能量，然後才開鎖。  
注意：開鎖不需要花費時間。  

時間複雜度 O(n! \* n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        ans = inf
        for p in permutations(strength):
            time = 0
            x = 1
            for req in p:
                time += (req+x-1) // x # wait energy
                x += K
            ans = min(ans, time)

        return ans
```

更快的做法是**狀壓 dp**。  

---

在枚舉開鎖順序時，不同的選擇順序可能會剩下相同的鎖，有**重疊的子問題**，考慮 dp。  
以 bitmask 表示鎖的狀態，0 代表沒開，1 代表已開。  

定義 dp(i, mask)：已開 i 個鎖，開剩下 N-i 個鎖的最小時間。  
轉移：dp(i, mask) = min(dp(i+1, new_mask) + time[j])，其中 time[j] = 開第 j 個鎖的時間。  
base：當 i = N 時，鎖全開完，回傳 0。  

答案入口 dp(0, 0)。  

時間複雜度 O(2^N \* N)。  
空間複雜度 O(2^N)。  

注意：狀態的 i 一定等同於 mask 的 bit 數，因此每個 mask 只會對應一種 i。  

```python
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        N = len(strength)

        @cache
        def dp(i, mask):
            if i == N:
                return 0
                
            x = 1 + K*i
            res = inf
            for j in range(N):
                if (1<<j) & mask == 0:
                    req = strength[j]
                    time = (req+x-1) // x
                    new_mask = mask | (1<<j)
                    res = min(res, dp(i+1, new_mask) + time)
            return res

        return dp(0, 0)
```
