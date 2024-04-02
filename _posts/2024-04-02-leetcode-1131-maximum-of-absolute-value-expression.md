---
layout      : single
title       : LeetCode 1131. Maximum of Absolute Value Expression
tags        : LeetCode Medium Array Math
---
曼哈頓距離練習題。雖然標 Medium，但我覺得光是數學就值 Hard。  

## 題目

輸入兩個等長的整數陣列。  
求滿足 0 <= i, j < arr1.length 的所有數對中，代入以下公式的最大值：  

- \|arr1[i] - arr1[j]\| + \|arr2[i] - arr2[j]\| + \|i - j\|  

## 解法

這公式其實可以理解成**三維**的曼哈頓距離。  
總之先把絕對值處理掉。  

以下將 arr1[i], arr1[j] 分別記做 x1, x2；  
arr2[i], arr2[j] 記做 y1, y2；  
i, j 記做 z1, z2。  

abs(x1 - x2) 等價於 max(x1 - x2, x2 - x1)。  
那麼 abs(x1 - x2) + abs(y1 - y2) 則等價於 max(x1 - x2, x2 - x1) + max(y1 - y2, y2 - y1)。  
等價於以下四者中取 max：  

- (x1 - x2) + (y1 - y2)  
- (x2 - x1) + (y1 - y2)  
- (x1 - x2) + (y2 - y1)  
- (x2 - x1) + (y2 - y1)  

基於**對稱性**，第一、四項等價，第二、三項等價。整理後變成：  

- (x1 + y1) - (x2 + y2)  
- -(x1 - y1) + (x2 - y2)  

---

最後還有一個 abs(z1 - z2)，等價於 max(z1 - z2, z2 - z1)。和剛才得出兩個結合：  

- (x1 + y1) - (x2 + y2) + (z1 - z2)  
- -(x1 - y1) + (x2 - y2) + (z1 - z2)  
- (x1 + y1) - (x2 + y2) + (z2 - z1)  
- -(x1 - y1) + (x2 - y2) + (z2 - z1)  

再整理一次：  

- (x1 + y1 + z1) - (x2 + y2 + z1)
- -(x1 - y1 - z1) + (x2 - y2 - z2)  
- (x1 + y1 - z1) - (x2 + y2 - z1)  
- -(x1 - y1 + z1) + (x2 - y2 + z2)  

可以看出，對於一組變數 (x, y, z) 轉換成三種形式，並維護其最大/最小值，再代入四個公式取最大值即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        A = [x + y + z for z, (x, y) in enumerate(zip(arr1, arr2))]
        B = [x - y - z for z, (x, y) in enumerate(zip(arr1, arr2))]
        C = [x + y - z for z, (x, y) in enumerate(zip(arr1, arr2))]
        D = [x - y + z for z, (x, y) in enumerate(zip(arr1, arr2))]
        
        ans = max(
            + max(A) - min(A),
            - min(B) + max(B),
            + max(C) - min(C),
            - min(D) + max(D)
        )
        
        return ans
```
