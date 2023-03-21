--- 
layout      : single
title       : LeetCode 2595. Number of Even and Odd Bits
tags        : LeetCode Easy Array BitManipulation
---
周賽337。正常的Q1真好。  

# 題目
輸入正整數n。  

令even為n的二進位表示中**偶數索引**出現1位元的次數。  
令odd為n的二進位表示中**奇數索引**出現1位元的次數。  

回傳answer陣列，其中answer = [even, odd]。  

# 解法
題目沒有講清楚二進位的索引是從左或右開始算，不太親切。  
根據例題中n = 2，二進位 = 10，answer = [0,1]可以確定最小位元為第0個索引。  

初始化長度為2的陣列ans，其中ans[0]代表偶數索引，ans[1]代表奇數索引。另外還有變數i代表當前奇偶。  
利用求餘運算將n轉成二進位，每次將餘數加入ans[i]中，再把i的奇偶性轉換。  

時間複雜度O(log n)。空間複雜度O(1)。  

```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans=[0,0]
        i=0
        
        while n>0:
            ans[i]+=n%2
            n//=2
            i^=1
            
        return ans
```
