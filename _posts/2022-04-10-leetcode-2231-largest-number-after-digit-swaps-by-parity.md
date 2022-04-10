---
layout      : single
title       : LeetCode 2231. Largest Number After Digit Swaps by Parity
tags 		: LeetCode Easy Array 
---
周賽288。近幾次來最整人的第一題。超多人以為是奇偶數位元互換，結果是所有奇數互換、所有偶數互換。

# 題目
輸入整數nums，你可以把nums中每個奇偶相同的數字互換位置，且可以換無限次，求透過換位可以得到的最大結果為多少。
例如：  
> 5724  
> 5和7可以換位，2和4可以換  
> 最大結果7542

# 解法
先把數字拆開成整數陣列，然後依奇偶分類、排序，再遍歷一次整數陣列，依照奇偶取出對應的最大數組成結果。

```python
class Solution:
    def largestInteger(self, num: int) -> int:
        odd=[]
        even=[]
        ns=[int(x) for x in str(num)]
        for n in ns:
            if n&1:
                odd.append(n)
            else:
                even.append(n)
                
        odd.sort()
        even.sort()
        ans=0
        for n in ns:
            if n&1:
                ans=ans*10+odd.pop()
            else:
                ans=ans*10+even.pop()
                
        return ans
```

