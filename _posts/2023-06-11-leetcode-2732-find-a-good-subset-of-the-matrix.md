--- 
layout      : single
title       : LeetCode 2732. Find a Good Subset of the Matrix
tags        : LeetCode Hard Array Matrix Bitmask BitManipulation HashTable
---
雙周賽106。被Q3搞到快死，根本沒時間看。  

# 題目
輸入m\*n的二進位矩陣grid。  

從grid選出某些列作為**非空**子集，如果子集中每列的總和都不超過子集大小的一半，則稱為**好子集**。  

正式的說，如果選出k個列作為子集，則每一行的總和最多為floor(k/2)。  

回傳構成**好子集**的列號，並以遞增排序。  
如果有好幾種**好子集**，選擇其中一種；如果不存在則回傳空陣列。  

# 解法
測資寫到n<=5，也就是最多5行。每個位置只能是0或1，那麼每列只有2^6種組合，不管再多列都只能是這32種，可以用bitmask表示狀態。  

例題很明顯的提示：如果某列全都是0，那就可以單獨以他構成**好子集**。反之，只要不全為0，是不可能用1列當成答案的。  
如果是2列，上限1：  
- 如果有某列為空，可以化簡到1列的情況  
- 否則這兩列**不可有交集**  
如果是3列，上限1.5下取整還是1：  
- 和2列的限制相同，還要多塞一列，那不如只選2列  
如果是4列，上限2：  
- 任意兩列都**必須有交集**，否則可以簡化成2列的情況  
- 考慮每列最少的列有1個1，如10000，其他只能是1xxxx。但是這樣一定超過上限  
- 每列最少有2個1，如11000，其他只能是10xxx或01xxx。但這樣第四列一定會超過上限  
- 每列最少有3個1，如11100，其他三個可以分別為100、010和001開頭。但又要滿足最少有三個1，後面兩位數都要填1，還是會超過上限  
- 每列最少有4個1，因為每行上限2，有5列，最多只能10個1，無法滿足4列且至少每列都有4個1
- 每列最少有5個1，就是全塞滿，不可能  
如果是5列，上限還是2：  
- 同樣上限2，連4列都塞不下，更不用說5列了  

結論，如果有空列就以該列為答案，否則找任意**無交集**的兩列；找不到就回傳空陣列。  

每次生成mask需要2^n，共m個。窮舉任意兩列為(2^n)^2，最多也才1024次運算。時間複雜度O(m \* 2^n)。  
空間複雜度O(2^n)。  

```python
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        N=len(grid[0])
        d={}
        
        for r,row in enumerate(grid):
            # build mask
            mask=0
            for i in range(N):
                mask|=(row[i]<<i)
            if mask==0:
                return [r]
            d[mask]=r
            
        for m1,r1 in d.items():
            for m2,r2 in d.items():
                if not m1&m2:
                    return sorted([r1,r2])
        
        return []
```
