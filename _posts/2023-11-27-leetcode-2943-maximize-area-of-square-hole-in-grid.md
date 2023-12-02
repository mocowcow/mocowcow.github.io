---
layout      : single
title       : LeetCode 2943. Maximize Area of Square Hole in Grid
tags        : LeetCode Medium Array Sorting Greedy
---
雙周賽118。剛開始看到一堆人答錯，沒人答對，感覺有陷阱。雖然的第一直覺是正確的，但是猶豫了好久。~~猶豫就會敗北~~。  

老實說題目描述有點垃圾。  
加上LC通常以m表示橫列、n表示直行，本題剛好相反，有點容易混淆。  

## 題目

輸入整數n和m。  
有一個網格，由n + 2個**水平**欄杆和m + 2個**垂直**欄杆組成，每個格子的面積都是1\*1。  
欄杆索引是由1開始計算。  

另外輸入兩個陣列hBars和vBars：  

- hBars由區間[2, n + 1]中的不同數所組成  
- vBars由區間[2, m + 1]中的不同數所組成  

你可以**移除**滿足以下條件的任意欄杆：  

- 包含在hBars中的水平欄杆  
- 包含在vBars中的垂直欄杆  

求移除任意欄杆後，能夠得到的**最大正方形**面積。  

## 解法

如果n=1，會有[1,2,3]共三個橫欄杆，且hBars範圍是[2, 2]。也就是外圍兩根一定不能被移除，不用考慮沒有最外圍的情形。  
重直欄杆同理。  

簡單來說：一個矩形內有n個橫欄杆、m個直欄杆，隔成若干個方正格子。  
然後hBars, vBars中對應可拆除的部分。  

題目要求一個**正方形**，那麼水平、垂直邊長必須相同。  
如果拆除連續的欄杆，則邊常會被合併。例如拆3,4,5號欄杆，得到1+1+1+1的邊；拆3,5,6號，得到長為1+1和1+1+1的邊。  
若不拆除，則最大邊長就是初始的1。  

因此找出兩方向中最長的邊，取兩者較小值作為正方形邊長，邊長平方即為答案。  

時間複雜度O(n log n + m log m)，瓶頸為排序。  
空間複雜度O(1)。  

```python
def f(bar):
    bar.sort()
    mx=0
    cnt=0
    prev=-inf
    for x in bar:
        if x==prev+1:
            cnt+=1
        else:
            cnt=1
        mx=max(mx,cnt)
        prev=x
    return mx+1

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h=f(hBars)
        v=f(vBars)
        side=min(h,v)
        
        return side**2
```

有個叫**分組循環**的技巧，適用於把陣列中的元素分成幾個相鄰的區段。  
外層迴圈枚舉左端點，內層迴圈擴展右端點。停止擴展後即可進行處理邏輯(本題為更新最大連續數)，然後更新左端點。  

```python
def f(bars):
    N=len(bars)
    bars.sort()
    i=0
    mx=0
    while i<N:
        j=i
        while j+1<N and bars[j]+1==bars[j+1]:
            j+=1
        mx=max(mx,j-i+1) # [i, j] in same group
        i=j+1
    return mx+1

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        return min(f(hBars),f(vBars))**2
```
