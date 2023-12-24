---
layout      : single
title       : LeetCode 2975. Maximum Square Area by Removing Fences From a Field
tags        : LeetCode Medium Array HashTable
---
周賽377。沒把debug用的print清乾淨，吃一個免費的OLE，太苦了。  

## 題目

有一個龐大的(m - 1) \* (n - 1)矩形場地，其左上角為(1,1)，右下角為(m,n)。  
陣列hFences和vFences分別代表裡面的水平、垂直柵欄。  

水平柵欄從(hFences[i], 1)延伸到(hFences[i], n)；垂直柵欄則從(1, vFences[i])延伸到(m, vFences[i])。  
簡單來說就是貫通整個場地。  

求**移除**任意圍欄(也可以不移除)後，可以得到的**最大正方形**面積。若無法組成正方形，則回傳-1。  
答案可能很大，先模10^9+7後回傳。  

注意：穿越四個角落的最外圈四個圍欄不可以被移除。  

## 解法

座標範圍高達10^9，不太好處理，先不管他。  

題目要求是正方形的面積，而那塊地的四周必須要有圍欄，才能算是合法的。  
換句話說，我們可以枚舉同一個維度的圍欄之間能夠組成的**邊長**。  

以範例1來說，水平圍欄位於x=[1,2,3,4]，垂直圍欄位於y=[1,2,3]。  
那任意兩根水平圍欄能夠組成的邊長共有[1,2,3,4]；任意兩根垂直圍欄的邊長共有[1,2,3]。  
這兩個維度的**共通邊長**有[1,2,3]，為了使面積盡可能大，選擇最大者，答案為3\*3=9。  

再來看例題2，水平x=[1,2,6]，垂直y=[1,4,7]。  
水平邊長有[1,4,5]；垂直邊長有[3,6]。  
兩者沒有共通邊長，無法組成正方形，答案為-1。  

兩個維度的處理邏輯相同，可以用一個函數f來求邊長。  
另外注意要自己把1和n(或m)座標的圍欄加上去。  
枚舉所有座標，其絕對差就是邊長。  

時間複雜度O(MX^2)，其中MX為max(len(hFences), len(vFences))。  
空間複雜度O(MX^2)。  

```python
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD=10**9+7
        
        def f(size,fs):
            fs.append(1)
            fs.append(size)
            s=set()
            for i in fs:
                for j in fs:
                    s.add(abs(i-j))
            return s
        
        hf=f(m,hFences)
        vf=f(n,vFences)
        union=hf & vf
        union.remove(0)        
        
        if len(union)==0:
            return -1
        
        x=max(union)
        
        return (x*x)%MOD
```
