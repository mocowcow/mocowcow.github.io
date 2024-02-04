---
layout      : single
title       : LeetCode 3030. Find the Grid of Region Average
tags        : LeetCode Medium Array Matrix Simulation
---
周賽383。囉嗦的模擬題，很可惜還是 WA 了一次。  

## 題目

輸入 m\*n 的網格 image，代表一個灰階圖片，其中 image[i][j] 代表一個像素的亮度。亮度都介於 [0..255]之間。  
另外還有非負整數 threshold。  

兩個像素 image[a][b] 和 image[c][d] 若滿足 |a - c| + |b - d| == 1，則稱為**相鄰**。  

**區域**指的是一個 3\*3的子網格，其中任意兩個**相鄰**像素的**絕對差**都小於等於 threshold。  
區域中的所有像素都屬於該區域，且一個像素可以數於多個區域。  

你必須計算出一個m\*n 的網格 result，其中 result[i][j] 是 image[i][j] 所屬區域的**平均亮度**，向下取整。  
若 image[i][j] 屬於多個區域，則 result[i][j] 是多個區域的**平均亮度**的**平均值**，向下取整。  
若 image[i][j] 不屬於任何區域，則 result[i][j] 等於 image[i][j]。  

求網格 result。  

## 解法

大致上還是個模擬題，照著做就可以。  

m\*n 的網格中會有 (m-2) \* (n-2) 個區域，枚舉所有區域，並對其中的像素計算貢獻。  
一個網格的平均亮度會同時貢獻給九個像素。一個像素可能數於多個區域，所以還要格外維護所屬的區域數。

主要麻煩的點在於：怎麼有效率的判斷一個區域中的所有**相鄰**像素的絕對差？  
與其檢查上下左右，其實可以只檢查每個像素的**右下**或是**左上**，擇一即可。  

我們枚舉區域的時候，是枚舉左上角 (i, j)，形成一個 3\*3 的正方形，因此這個正方形的右邊界是 i+2，下邊界是 j+2。  
因此，對於區域中每個的像素，只要其右方、下方不超出這個界限，就要檢查絕對差。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        
        def reg(i, j): # upper left point of region
            sm = 0
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    sm += image[ii][jj]
                    if ii + 1 < i + 3: # check down
                        if abs(image[ii][jj] - image[ii + 1][jj]) > threshold:
                            return -1
                    if jj + 1 < j + 3: # check right
                        if abs(image[ii][jj] - image[ii][jj + 1]) > threshold:
                            return -1
            return sm // 9  
        
        M, N = len(image), len(image[0])
        inten = [[0] * N for _ in range(M)]
        cnt = [[0] * N for _ in range(M)]
        
        for i in range(M - 2):
            for j in range(N - 2):
                val = reg(i, j)
                if val == -1: # not region
                    continue
                    
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        inten[ii][jj] += val 
                        cnt[ii][jj] += 1
                        
        ans = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if cnt[i][j] == 0:
                    ans[i][j] = image[i][j]
                else:
                    ans[i][j] = inten[i][j] // cnt[i][j]
                    
        return ans
```
