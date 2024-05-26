---
layout      : single
title       : LeetCode 3160. Find the Number of Distinct Colors Among the Balls
tags        : LeetCode Medium Array HashTable Simulation
---
雙周賽 131。和 Q2 差不多的奇怪 Q3。但有一個小陷阱，而且我還中了，可悲。  

## 題目

輸入整數 limit 和二維整數陣列 queries。  

有 limit + 1 個球，編號分別為 [0, limit]，起初所有球都沒有顏色。  
每次查詢的格式為 [x, y]，代表要將第 x 個球改成顏色 y，然後求當前有多少種**不同的顏色**。  

回傳陣列 result，其中 result[i] 代表第 i 次查詢的結果。  

注意：沒有顏色的球並不算是一種顏色。  

## 解法

我們需要維護所有球的顏色，但是球超級多，**不能用陣列**，只能用雜湊表。  

另外還要維護每個**顏色的出現次數**，還有**顏色種類** cnt。  
當顏色 y 出現第一次的時候增加 cnt；反之，改變顏色後，使得顏色 y 不存在時，減少 cnt。  

時間複雜度 O(Q)。  
空間複雜度 O(Q)。  

```python
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color = Counter()
        color_freq = Counter()
        cnt = 0
        ans = []

        for x, y in queries:
            # clean old color 
            old_y = color[x]
            if old_y != 0:
                color_freq[old_y] -= 1
                if color_freq[old_y] == 0:
                    cnt -= 1

            # paint new color
            color[x] = y
            color_freq[y] += 1
            if color_freq[y] == 1:
                cnt += 1

            ans.append(cnt)

        return ans
```

直接拿雜湊表大小計算不同顏色更加簡潔。  

```python
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color = Counter()
        color_freq = Counter()
        ans = []

        for x, y in queries:
            # clean old color 
            old_y = color[x]
            if old_y != 0:
                color_freq[old_y] -= 1
                if color_freq[old_y] == 0:
                    del color_freq[old_y]

            # paint new color
            color[x] = y
            color_freq[y] += 1

            ans.append(len(color_freq))

        return ans
```
