--- 
layout      : single
title       : LeetCode 2429. Minimize XOR
tags        : LeetCode Medium BitManipulation Greedy
---
周賽313。哩扣最愛的位元運算又來了，連續好幾周都有他的戲。  

# 題目
輸入兩個正整數num1和num2，找到符合以下條件的整數x：  
- x和num2所擁有的**置位數**相同  
- x和num1做XOR運算後得到的值最小  

回傳整數x。題目保證x是唯一一個答案。  
整數的**置位數**指的是其二進制表示中1 bit的數量。  

# 解法
再來複習一次XOR的特性：兩兩相消，相同的bit會得到0，不同的bit得到1。  
x和num2有相同的置位數，那第一步當然是求出num2有多少個置位。  
要使得num1和x做XOR的結果較小，那就要盡可能的將num1中較大的1 bit變成0，可以減少更多值。  
從num1的最高位元(MSB)開始檢查，如果其為1，則將x的相同位置也設成1。  

但是num1的置位數可能比num2還小，刪掉num1中的所有1 bit還不夠，還得在其他位置上也放上1 bit。  
和剛才相反，這次放上的1 bit會使得XOR結果變大，所以要從較低的位元(LSB)開始往左找。若其位置為0，則將x的相同位置設成1。  

數據範圍10^9，最多30個位元，可視為常數時間。時空間複雜度O(1)。  

```python
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt=num2.bit_count()
        x=0
        
        for i in reversed(range(30)):
            if cnt==0:break
            if (1<<i)&num1:
                x|=(1<<i)
                cnt-=1
        
        for i in range(30):
            if cnt==0:break
            if not (1<<i)&num1:
                x|=(1<<i)
                cnt-=1
        
        return x
```
