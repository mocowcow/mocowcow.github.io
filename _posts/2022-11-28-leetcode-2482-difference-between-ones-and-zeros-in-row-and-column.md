--- 
layout      : single
title       : LeetCode 2482. Difference Between Ones and Zeros in Row and Column
tags        : LeetCode Medium Array Medium Simulation
---
雙周賽92。矩陣內的元素是整數0，但是我把判斷式打成字元"0"，浪費一堆時間debug，太憨了。  

# 題目
輸入m\*n的矩陣grid。  

依照以下規則產生m\*n的矩陣diff：  
- oneRow<sub>i</sub>等於第i列的1數量  
- oneCol<sub>j</sub>等於第j行的1數量  
- zeroRow<sub>i</sub>等於第i列的0數量  
- zeroCol<sub>j</sub>等於第j行的0數量  
- diff[i][j] = onesRow<sub>i</sub> + onesCol<sub>j</sub> - zerosRow<sub>i</sub> - zerosCol<sub>j</sub>  

回傳矩陣diff。  

# 解法
很間單的模擬題，照著敘述做就可以。  
第一次遍歷矩陣，計算各行列的0與1數量。因為元素已經讀取完成，第二次遍歷可以直接將答案寫在grid上，最後回傳grid。  

時間O(MN)，空間至少需要長度M和N的陣列計數，所以是O(min(M,N))。  

```python
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        M,N=len(grid),len(grid[0])
        r0=[0]*M
        r1=[0]*M
        c0=[0]*N
        c1=[0]*N
        
        for r in range(M):
            for c in range(N):
                if grid[r][c]==0:
                    r0[r]+=1
                    c0[c]+=1
                else:
                    r1[r]+=1
                    c1[c]+=1
                    
        for r in range(M):
            for c in range(N):
                grid[r][c]=r1[r]+c1[c]-r0[r]-c0[c]
        
        return grid
```
