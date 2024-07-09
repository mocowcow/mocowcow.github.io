---
layout      : single
title       : LeetCode 3206. Alternating Groups I
tags        : LeetCode Easy Array Simulation
---
雙周賽 134。

## 題目

有個由紅藍瓷磚組成的圓環。  
輸入整數陣列 colors。其中 colors[i] 代表第 i 個磁磚的顏色：  

- colors[i] == 0 代表磁磚 i 是紅色  
- colors[i] == 1 代表磁磚 i 是藍色  

每 3 個連續且**顏色交替**的磁磚稱作**交替組**。  

求有多少個**交替組**。  

注意：由於是環狀，最後一個磁磚和第一個磁磚被視為相鄰的。  

## 解法

暴力模擬。  
枚舉每個索引 i 作為群組的第三個磁磚，檢查前兩個磁磚 i-1, i-2 顏色是否交替即可。  

注意：py 支援負數索引，其他語言需要對 N 取餘數避免出界。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        N = len(colors)
        ans = 0
        for i in range(N):
            if colors[i] != colors[i - 1] != colors[i - 2]:
                ans += 1

        return ans
```
