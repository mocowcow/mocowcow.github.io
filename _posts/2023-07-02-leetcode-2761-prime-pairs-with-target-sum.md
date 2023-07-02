--- 
layout      : single
title       : LeetCode 2761. Prime Pairs With Target Sum
tags        : LeetCode Medium Array Math TwoPointers HashTable
---
雙周賽352。

# 題目
輸入整數n。  
若整數x和y滿足以下條件，則稱為**質數對**：  
- 1 <= x <= y <= n  
- x + y = n  
- x和y都是質數  

找到所有的質數對[x<sub>i</sub>, y<sub>i</sub>]，並依x<sub>i</sub>**遞增排序**。  
如果不存在質數對，則回傳空陣列。  

# 解法
總之先找出小於n的所有質數。  

使用雙指針，分別從最大和最小的質數l和r開始配對：  
- p[l]+p[r]=n，加入答案，兩個指針都移動  
- p[l]+p[r]>n，需要將和減少，r左移  
- p[l]+p[r]<n，需要將和增加，l右移  

質數篩複雜度O(n log log n)，而n以內有O(n / log n)個質數。  
時間複雜度O(n log log n)。  
空間複雜度O(n / log n)。  

```python
def get_prime(n):
    sieve = [True]*(n+1)
    prime = []
    for i in range(2, n+1):
        if sieve[i]:
            prime.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return prime

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        p=get_prime(n)
        ans=[]
        l=0
        r=len(p)-1
        while l<=r:
            sm=p[l]+p[r]
            if sm==n:
                ans.append([p[l],p[r]])
                l+=1
                r-1
            elif sm>n:
                r-=1
            else: # sm<n
                l+=1
                
        return ans
```
