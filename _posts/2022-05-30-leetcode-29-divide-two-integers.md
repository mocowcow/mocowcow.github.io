--- 
layout      : single
title       : LeetCode 29. Divide Two Integers
tags        : LeetCode Medium Math BitManipulation
---
每日題。這題從好久以前就看過了，沒什麼想法，而且還超多爛，就沒想碰他。竟然出現在每日題，看來會增加更多爛。

# 題目

輸入兩個整數dividend和divisor，在不使用乘法、除法和模運算的情況下將兩個整數相除。  
整數除法必須取整，正數無條件捨去，負數無條件進位。例如：  
> 8.345 = 8  
> -2.7335 = -2  

回傳計算完的商。  
注意：整數範圍為[−2^31, (2^31)−1]，如果商大於(2^31)−1，則回傳(2^31)−1；如果商小於-2^31則回傳-2^31。  

# 解法
自己試了幾次還是不對，就找個解法來看了。  
個人覺得第一行判斷正負數的方式非常厲害，算是今天最大的收穫。  

首先判斷商的正負號，並將兩個都先轉成正整數。  
再來處理edge case，當分母為1時，直接回傳被除數。  
需要注意的是，當被除數為-2147483647，而除數為-1時，會超出題目規定的邊界，所以要和(2^31)-1取最小值，避免出界。  

剩下只要以被除數不斷扣除**除數的倍數**，直到被除數小於除數為止。  
因為一次一次扣非常沒有效率，可以試著**將除數翻倍成長**，減少計算次數。  
最後根據正負號調整商，就是正確答案。  

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive=(dividend<0)==(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        if divisor==1:
            if positive:
                return min(dividend,2147483647)
            else:
                return -dividend
            
        ans=0
        n=divisor
        while dividend>=divisor:
            t=divisor
            cnt=1
            while dividend>=t:
                dividend-=t
                ans+=cnt
                t<<=1
                cnt<<=1
          
        if not positive:
            ans=-ans
            
        return ans
```
