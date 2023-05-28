--- 
layout      : single
title       : LeetCode 2713. Maximum Strictly Increasing Cells in a Matrix
tags        : LeetCode Hard Array HashTable DP Sorting
---
周賽347。雙周單周賽都AK，而且還在200名內，最近運氣不錯。  

# 題目
輸入m\*n的整數矩陣mat，你可以選擇任意格子作為起點。  
從起點出發，你可以不斷移動到**同一行**或**同一列**的其他格子，但目標格子的值必須**嚴格大於**當前格子。 

你的目標是找到可以訪問**最多格子**的起點。  

回傳最多可以訪問多少格子。  

# 解法
乍看很像普通的dfs，但每個格子有M+N個選項，複雜度會高達O(MN\*(M+N))，大約10^10次運算，肯定不行。  

先考慮最極端的情況，所有元素都在一列，例如：  
> [1,2,3,4]或是[1,2,4,3]之類的排列  
> 從最小值1出發，步數1，這時列最大步數為1  
> 再來是2，可以從任何較小的格子移動過來  
> 所以移動到2的步數為最大步+1，也就是2  
> 3的步數為最大步+1，等於3  
> 4的步數為最大步+1，等於4  

發現只要按照遞增順序訪問，同時更新列最大步數，可以保證先前訪問過的格子值一定較小，所以當前格子步數為**列最大步+1**。  
那如果有重複的值呢？例如：  
> [1,1,2]  
> 需要處理完所有的1，才能更新列最大步數  
> 2的最大步數應該為2  

行也是同樣道理，需要維護各行列的最大步數。  
完整步驟如下：  
1. 將各格子索引(r,c)以grid[r][c]為鍵值分組  
2. 以遞增順序處理各組。求出組內所有位置的步數後，再更新各行列的最大步數  
3. 等所有索引都處理完，找到各行列最大步數即可  

瓶頸在於排序，時間複雜度O(MN log MN)。  
空間複雜度O(M+N)。  

```python
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        M,N=len(mat),len(mat[0])
        steps=[[0]*N for _ in range(M)]
        row=[0]*M
        col=[0]*N
        
        d=defaultdict(list)
        for r in range(M):
            for c in range(N):
                d[mat[r][c]].append([r,c])
        
        ans=0
        for k in sorted(d):
            for r,c in d[k]:
                steps[r][c]=max(row[r],col[c])+1
                ans=max(ans,steps[r][c])
            for r,c in d[k]:
                row[r]=max(row[r],steps[r][c])
                col[c]=max(col[c],steps[r][c])
                
        return ans
```
