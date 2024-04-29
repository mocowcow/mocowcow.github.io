---
layout      : single
title       : LeetCode 3127. Make a Square with the Same Color
tags        : LeetCode Easy Array Matrix HashTable
---
雙周賽 129。

## 題目

輸入 3 \* 3 的二維整數陣列 grid，其中只包含字元 'B' 和 'W' ，分別代表黑色和白色。  

你最多可以改變一個格子的顏色，並試著使得任意 2 \* 2 的正方形區域呈現同一種顏色。  

若能得到相同顏色的 2 \* 2 的正方形則回傳 true；否則回傳 false。  

## 解法

3 \* 3 區塊中只有 4 個 2 \* 2 正方形，枚舉所有正方形並統計顏色頻率。  

若某個顏色出現 3 次，可以透過一次操作使得四格同色；若原本四格就同色當然更好。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                d = Counter()
                d[grid[r][c]] += 1
                d[grid[r + 1][c]] += 1
                d[grid[r][c  +1]] += 1
                d[grid[r + 1][c + 1]] += 1
                if d["B"] >= 3 or d["W"] >= 3:
                    return True
                
        return False
```

有些大神只統計其中一個顏色的頻率，看起來更簡潔。  

只考慮黑色的頻率 cnt：  

- cnt = 0，白色頻率 4，合法  
- cnt = 1，白色頻率 3，合法  
- cnt = 2，白色頻率 2，不合法  
- cnt = 3，白色頻率 1，合法  
- cnt = 4，白色頻率 0，合法  

只要頻率不為 4 都合法。  

```python
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                cnt = 0
                for dx in range(2):
                    for dy in range(2):
                        if grid[r + dx][c + dy] == "B":
                            cnt += 1
                if cnt != 2:
                    return True
                
        return False
```
