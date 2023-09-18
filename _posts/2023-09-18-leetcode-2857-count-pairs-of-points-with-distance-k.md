---
layout      : single
title       : LeetCode 2857. Count Pairs of Points With Distance k
tags        : LeetCode Medium Array Matrix BitManipulation HashTable
---
雙周賽113。

## 題目

輸入**二維**整數陣列coordinates和整數k，其中coordinates[i] = [x<sub>i</sub>, y<sub>i</sub>]，代表第i個點位於二維平面上的座標。  

定義兩點(x1, y1)和(x2, y2)之間的**距離**為(x1 XOR x2) + (y1 XOR y2)，其中XOR是位元異或運算。  

求有多少個數對(i, j)滿足i < j且距離等於k。  

## 解法

總共有50000個點，要暴力求出每個座標間的距離不太理想。  
但是k只有100，這應該會是一個突破口。  

(x1 XOR x2) + (y1 XOR y2) = k，可以把k分成l + r兩個數，當作兩個式子：  

- x1 XOR x2 = p 移項得到 x2 = x1 XOR p  
- y1 XOR y2 = q 移項得到 y2 = y1 XOR q  

遍歷每個點(x1, y1)，並枚舉所有pq組合，計算有多少出現過的點滿足(x2, y2)。  

時間複雜度O(N \* k)。  
空間複雜度O(N)。  

```python
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        d=Counter()
        ans=0
        for x,y in coordinates:
            for p in range(k+1):
                q=k-p
                ans+=d[(x^p,y^q)]
            d[(x,y)]+=1
            
        return ans
```

對於其他不支援tuple做雜湊的語言，可以把x座標加上一個大於座標最大值的offset，紀錄在一個整數中，例如：  
> (x, y) = (7, 5), offset = 10^7  
> coor = 7\*10^6 + 5  
> coor = 7000005  

或是對x位元移位也可以。  

```python
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        offset=32
        d=Counter()
        ans=0
        for x,y in coordinates:
            coor=(x<<32)+y
            for p in range(k+1):
                q=k-p
                ans+=d[((x^p)<<32)+(q^y)]
            d[coor]+=1
            
        return ans
```
