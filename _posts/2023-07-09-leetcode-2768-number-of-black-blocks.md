--- 
layout      : single
title       : LeetCode 2768. Number of Black Blocks
tags        : LeetCode Medium Array Matrix HashTable
---
雙周賽108。還挺妙的題，考慮太多反而會寫得太複雜。  

# 題目
輸入兩個整數m和n，代表一個m\*n的矩陣。  

還有一個二維的矩陣座標，其中coordinates[i] = [x, y]，代表矩陣的[x, y]格子是**黑色**的。沒在coordinates中出現的其餘格子都是**白色**。  

**區塊**指的是一個2\*2的子矩陣。更正式地說，滿足0 <= x < m - 1且0 <= y < n - 1，並以[x, y]為左上角的區塊，包含了[x, y], [x + 1, y], [x, y + 1]和[x + 1, y + 1]四個格子。  

回傳長度為5的陣列arr，其中arr[i]代表**擁有i個黑色格子**的區塊數量。  

# 解法
一個區塊會包含4個格子，換句話說，一個格子可能會對4個區塊產生影響。  
而有效的區塊位置不可以是最後一行或是最後一列。  

維護雜湊表，記錄各區塊的黑色格子數量。  
遍歷coordinates中的座標x,y，並窮舉四個可能的區塊位置，如果是合法的區塊，則將其黑色計數+1。  

先求出所有的區塊數，扣掉有黑色的區塊數，剩下就是沒有黑色的區塊數量。  

時間複雜度O(Q)，其中Q為coordinates長度。  
空間複雜度O(Q)。  

```python
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        d=Counter()
        tot=(m-1)*(n-1)
        
        for x,y in coordinates:
            for dx in range(2):
                for dy in range(2):
                    xx=x-dx
                    yy=y-dy
                    if 0<=xx<m-1 and 0<=yy<n-1:
                        d[(xx,yy)]+=1

        ans=[0]*5
        for v in d.values():
            ans[v]+=1
            tot-=1
            
        ans[0]=tot
            
        return ans
```
