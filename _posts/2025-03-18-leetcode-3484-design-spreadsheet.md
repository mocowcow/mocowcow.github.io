---
layout      : single
title       : LeetCode 3484. Design Spreadsheet
tags        : LeetCode Medium Simulation HashTable
---
biweekly contest 152。  
非常妙的題，根據做法不同，麻煩程度差非常多。  

## 題目

<https://leetcode.com/problems/design-spreadsheet/description/>

## 解法

一看就是類似 excel 的表格。  
但是很良心，列數只有從 A-Z，沒有奇怪的 AFZXC 這種列號，不需要把列號轉換回整數。  
也只有單格修改，沒有範圍修改。  
甚至只有加法函數。  

有些同學可能很老實，自己開了個 row \* col 陣列來當表格。  
其實直接拿 cell 當作 key 拿去**雜湊表**就好。  

實際上只需要做兩個功能：  

- parse(String s)：若 s 是 cell 則回傳對應值；否則解析成整數。  
- getValue(String formula)：把 formula 拆成兩個字串 parse 後加總。  

時間複雜度 O(N)，其中 N 為不同的 cell 個數。  
空間複雜度 O(N)。  

```python
class Spreadsheet:

    def __init__(self, rows: int):
        self.d = Counter()

    def setCell(self, cell: str, value: int) -> None:
        self.d[cell] = value

    def resetCell(self, cell: str) -> None:
        del self.d[cell]

    def getValue(self, formula: str) -> int:
        A, B = formula[1:].split("+")
        return self.parse(A) + self.parse(B)

    def parse(self, cell):
        if cell.isdigit():
            return int(cell)
        else:
            return self.d[cell]
```
