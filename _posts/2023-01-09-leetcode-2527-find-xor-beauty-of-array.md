--- 
layout      : single
title       : LeetCode 2527. Find Xor-Beauty of Array
tags        : LeetCode Medium Array BitManipulation
---
雙周賽95。又是大家最愛的位元運算，喜聞樂見。  

# 題目
輸入整數陣列nums。  

定義三個索引i, j, k的**有效值**定義為((nums[i] | nums[j]) & nums[k])。  

陣列的**XOR美麗值**為所有滿足0 <= i, j, k < n的三元組(i, j, k)的**有效值**的XOR結果。  

求nums的XOR美麗值。  

# 解法
重新複習一下，XOR的特性是**兩兩相消**。  

1. 先看看nums[i] | nums[j]的部分，因為每個索引都會出現一次，所以必定會出現nums[j] | nums[i]。而這兩個結果做XOR會直接被抵銷掉，所以只要考慮i==j的情況，問題簡化成所有(nums[i] & nums[k])的XOR結果。  
2. 同理，對於所有nums[i] & nums[k]，也存在nums[k] & nums[i]為同樣的值。兩者會互相抵消，問題簡化成所有nums[i]的XOR結果。  
3. 直接對nums中所有數字做XOR即可。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans=0
        for n in nums:
            ans^=n

        return ans
```
