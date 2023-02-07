--- 
layout      : single
title       : LeetCode 2556. Disconnect Path in a Binary Matrix by at Most One Flip
tags        : LeetCode Medium Array Matrix DFS
---
雙周賽97。第三題想不出，剩下最後5分鐘發現這題比較簡單，沒時間做了。  

# 題目
輸入m\*n的二進位矩陣grid。你可以從(row, col)移動到(row + 1, col)或是(row, col + 1)，且其值為1的格子。若你無法從(0, 0)抵達(m - 1, n - 1)，則稱為**不連通**。  

你可以將**最多一個**(也可能零個)格子的值**翻面**，但不可以翻(0, 0)和(m - 1, n - 1)。  

如果你可以使得矩陣變成**不連通**，則回傳true，否則回傳false。  

注意：將一個格子**翻面**會使得其值從0變成1，或是從1變成0。  

# 解法
雖說0和1都可以翻面，但是把0翻成1不僅沒辦法使得路徑減少，反而有可能使得矩陣連通，因此只考慮把1翻成0。  

最理想的狀況當然是矩陣本來就不連通。或是只有一條抵達的路徑，這樣無論如何，翻轉任意的1都可以使其不連通。  
如果有兩條以上的不重疊路徑，不管切斷哪條，都會剩下其他條可以走，此矩陣將永遠連通。  
那如果有多條路徑，但是都在某個點交會，是不是翻轉那個交會點就不連通了？  

![示意圖](/assets/img/2556-1.jpg)  

用想的很簡單，但是要怎麼找到這個關鍵點？  
這種只能向下、向右走的題目有個關鍵點：總步數一定是M+N-2步。所以我們只要確保每一步中，有任一步不存在2種以上的可能位置，那就有可能成為**不連通**圖。  

![示意圖](/assets/img/2556-2.jpg)  

所以我們直接從起點開始dfs，每抵達一個新的位置，就將其對應的步數計數+1。  
除了起點與終點以外，每個步數都應該至少存在2個以上的可能位置，所以從第1步檢查到M+N-3步。  
若其中一步不符合，回傳true；否則代表存在多條路徑，回傳false。    

時間複雜度O(M\*N)。空間複雜度O(M\*N)。  

```python
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        M,N=len(grid),len(grid[0])
        step=[0]*(M+N)
        
        @cache
        def dfs(r,c):
            if r<0 or r==M or c<0 or c==N:
                return
            if grid[r][c]==0:
                return 
            step[r+c]+=1
            dfs(r+1,c)
            dfs(r,c+1)
        
        dfs(0,0)
        
        for i in range(1,M+N-2):
            if step[i]<2:
                return True
            
        return False
```