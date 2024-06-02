---
layout      : single
title       : LeetCode 3168. Minimum Number of Chairs in a Waiting Room
tags        : LeetCode Easy Array String Simulation
---
周賽 400。

## 題目

輸入字串 s。模擬每秒發生的事件：  

- 如果 s[i] == 'E'，代表有一個人進入房間，並拿一張椅子坐下  
- 如果 s[i] == 'L'，代表有一個人離開房間，讓出一張椅子  

求**最少**需要準備幾張椅子，才能確保房間內每個人都有位置坐。  

## 解法

模擬人流，看房間內同時最多有幾個人。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumChairs(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == "E":
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt -= 1
                
        return ans
```
