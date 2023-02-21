--- 
layout      : single
title       : LeetCode 2571. Minimum Operations to Reduce an Integer to 0
tags        : LeetCode Medium Greedy BitManipulation
---
周賽333。這題原本標的是難度是easy，搞得一堆人心裡崩潰，一點都不easy。  

# 題目
輸入正整數n，你可以進行以下動作數次：  
- 對n增加或是減去**2的冪次數**  

求使得n變成0所需的**最小動作次數**。  

# 解法
說到2的冪次數，這些數字必定只有一個1位元。可以理解為對某個位置增加/減少1位元。  

從例題1的39來研究：  
> n = 39, 二進位 = 100111  
> 加上1，得到101000  
> 減掉1000，得到100000  
> 減掉100000，得到0  

發現單獨的1只能直接減掉，而連續出現的1可以先透過一次增加使之連續進位，最後變成一個1。  
而每個進位後只會影響左方的位元，因此從最小的位元(LSB)開始向左遍歷，若找到連續的1位元則使之進位；單獨的1位元則直接刪除。  

時間複雜度O(log n)。空間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        
        for i in range(20):
            if n&(1<<i):
                ans+=1
                if n&(1<<(i+1)):
                    n+=(1<<i)
                else:
                    n-=(1<<i)
            
        return ans
```
