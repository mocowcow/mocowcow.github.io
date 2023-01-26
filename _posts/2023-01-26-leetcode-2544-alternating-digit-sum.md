--- 
layout      : single
title       : LeetCode 2544. Alternating Digit Sum
tags        : LeetCode Easy
---
周賽329。

# 題目
輸入正整數n。對於n的每個數字會按照以下規則分配正負號：  
- 最左邊的數字會是**正號**  
- 剩下數字都和其左邊的數字正負號相反  

求所有數字配上對應符號的總和。  

# 解法
方便起見，直接把n轉成字串，再從字串中每一個字元分別轉回數字，並加上正負號，加入答案。  

時間複雜度O(log n)。空間複雜度O(log n)。  

```python
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign=1
        ans=0
        
        for c in str(n):
            ans+=sign*int(c)
            sign*=-1
            
        return ans
```

雖然說可以直接透過取餘數來拆出各個數字，但是正負號是從最高位開始計算，取餘數是從最低位，因此會找不到對應的符號。  

參考了大神的想法：一樣是從最低位開始正、負輪流取，結束時如果最後一個數字是負號，則代表全部的數都要取反，例如：  
> n = 23  
> 第一個餘數3，正號  
> 第一個餘數2，負號  
> sum = 3 + (-2) = 1  
> 但最後一個數字負號，所以取反，sum = -1  

時間複雜度O(log n)。空間複雜度O(1)。  

```python
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign=1
        ans=0
        
        while n>0:
            r=n%10
            ans+=r*sign
            sign*=-1
            n//=10
            
        return ans*-sign
```
