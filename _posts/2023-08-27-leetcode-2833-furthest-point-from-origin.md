---
layout      : single
title       : LeetCode 2833. Furthest Point From Origin
tags        : LeetCode Easy String Greedy
---
周賽360。

## 題目

輸入長度n，由'L', 'R', 和 '_'組成的的字串moves。  
代表你從起點0出發之後的一連串移動。  

對於第i次移動：  

- 如果moves[i]是'L'或'_'，可以向左走  
- 如果moves[i]是'R'或'_'，可以向右走  

求經過n次移動後，最遠能夠距離起點多少單位。  

## 解法

對於'L'和'R'沒有選擇，只能照指定方向走，唯一能選擇的是'_'走哪邊。  
L和R方向相反會抵消，看偏向哪方，剩下的所有'_'也走同一個方向。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=moves.count("L")
        r=moves.count("R")
        space=moves.count("_")
        
        return abs(l-r)+space
```

歡樂一行版本。  

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("L")-moves.count("R"))+moves.count("_")
```
