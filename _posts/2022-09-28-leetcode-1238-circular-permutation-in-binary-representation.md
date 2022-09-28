--- 
layout      : single
title       : LeetCode 1238. Circular Permutation in Binary Representation
tags        : LeetCode Medium BitManipulation Math
---
每日題。[89. gray code]({% post_url 2022-09-28-leetcode-89-gray-code %})的變種。  
這題似乎是某次周賽的Q2，說實話是有點過分，沒做過原題的八成直接陣亡。  

# 題目
給輸入兩個整數n和start，找到數列[0,2^n-1]的任意排列p，並符合：  
- p[0]=start
- p[i]和p[i+1]在二進制中只有一個位元不同  
- p[0]和p[2^n-1]在二進制中只有一個位元不同  

# 解法
先求出n位的格雷碼，找到start的索引位置idx，將數列翻轉即可。  

時空間複雜度O(2^n。  

```python
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        def grayCode(n):
            ans=[0,1]
            for i in range(n-1):
                add=1<<(i+1)
                ans+=[x|add for x in reversed(ans)]
            return ans

        ans=grayCode(n)
        idx=ans.index(start)
        
        return ans[idx:]+ans[:idx]
```
