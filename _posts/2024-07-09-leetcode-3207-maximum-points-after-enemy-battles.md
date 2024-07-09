---
layout      : single
title       : LeetCode 3207. Maximum Points After Enemy Battles
tags        : LeetCode Medium Array Sorting Greedy
---
雙周賽 134。

## 題目

輸入整數陣列 enemyEnergies，代表各個敵人的體力值。  
另外還有整數 currentEnergy，代表你的初始體力值。  

最初你的分數為 0，且所有敵人都是**未標記**的。  
你可以執行以下操作任意次來獲取分：  

- 選擇**未標記**的敵人 i，且 currentEnergy >= enemyEnergies[i] 然後：  
  - 你會獲得 1 分  
  - 你的體力會減少 enemyEnergies[i]  

- 若你擁有**至少 1 分**，則可選擇**未標記**的敵人 i，然後：  
  - 你的體力會增加 enemyEnergies[i]  
  - **標記**敵人 i  

求通過以上操作，最多可以獲得多少分。  

## 解法

第一種操作相當於找敵人**練等**，可以一練再練，不斷刷錢。  
第二種操作則是把敵人**丟掉** (?)，丟掉之後就不能再找他了。  

關鍵點是**同一個敵人可以練多次**：既然收穫都一樣，那就找最弱的揍！  

---

初始分數固定是 0，一定要**先練等**一次才能**丟掉**。  
如果初始體力連最弱的敵人都打不了，可以直接回家了。答案是 0。  

否則可以一值打最弱的敵人，體力不夠就把最強的賣掉，不斷重複即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        a = sorted(enemyEnergies)
        if a[0] > currentEnergy:
            return 0
        
        e = currentEnergy
        ans = 0
        while a:
            if e >= a[0]:
                x = e // a[0]
                ans += x
                e -= a[0] * x
            else:
                e += a.pop()
                
        return ans
```
