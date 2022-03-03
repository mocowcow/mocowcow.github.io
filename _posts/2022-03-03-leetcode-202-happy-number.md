---
layout      : single
title       : LeetCode 202. Happy Number
tags 		: LeetCode Easy HashTalbe Math
---
Study Plan - Programming Skills。  

# 題目
整數n，每次將n的每個位數平方後加總，若最後能夠變成1，則n為快樂數。求n是不是快樂數。  

# 解法
不是快樂數的話會陷入死循環，例如[3,9,81,65,..,61,37,58,..,16,37]，37之後無限循環。  
維護集合seen，將出現過的n加入seen，若重複出現即回傳false，成功讓n=1則回傳True。

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            t = 0
            while n > 0:
                t += (n % 10)**2
                n //= 10
            n = t

        return True
```
