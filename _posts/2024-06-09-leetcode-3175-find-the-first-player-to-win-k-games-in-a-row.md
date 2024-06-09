---
layout      : single
title       : LeetCode 3175. Find The First Player to win K Games in a Row
tags        : LeetCode Medium Array Simulation
---
雙周賽 132。

## 題目

一場比賽共有 n 個選手，編號分別從 0 到 n - 1。  

輸入長度 n 的整數陣列 skills，其中 skills[i] 代表第 i 個選手的強度，保證每個人強度都不同。  
另外還有正整數 k。  

最初，所有選手按照編號排隊。  
比賽過程如下：  

- 最前面的兩個選手比賽，強度高的人贏  
- 結束後，贏家繼續留在隊伍最前方，輸家去最後方排隊  

求第一個連續贏 k 次的選手編號。  

## 解法

雙端隊列可以模擬比賽過程。  
但是在 k 很大的情況下，直接模擬會超時，並且只有最強的選手會無限虐菜。  
因此在所有選手都比過一次後，若還沒人達成 k 連勝，則最後贏家肯定是最強那位 (也就是隊列中第一位)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        N = len(skills)
        q = deque(range(N))
        win = [0] * N
        
        while len(q) >= 2:
            i = q.popleft()
            j = q.popleft()
            # keep skill i > j
            if skills[i] < skills[j]:
                i, j = j, i
            win[i] += 1
            q.appendleft(i)
            if win[i] == k:
                return i
            
        return q[0]
```
