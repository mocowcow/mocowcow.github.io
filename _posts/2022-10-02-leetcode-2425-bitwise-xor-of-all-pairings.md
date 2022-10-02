--- 
layout      : single
title       : LeetCode 2425. Bitwise XOR of All Pairings
tags        : LeetCode Medium Array BitManipulation
---
雙周賽88。最近周賽常常出現什麼位元XOR、OR還是AND，快麻痺了。  

# 題目
輸入兩個由非負整數組成的陣列nums1和nums2。存在另一個陣列nums3，由nums1和nums2之間的所有整數數對的位元XOR結果所組成(nums1中每個整數與nums2中的每個整數恰好配對一次)。  

回傳nums3中所有XOR後的總和。  

# 解法
XOR最重要的特性就是兩兩相消。  
每個nums1[i]都會和每個nums2[j]組成數對。如果nums2的長度為偶數，所有nums1[i]都會被相消掉；同理，如果nums1的長度為偶數，所有nums2[j]都會被相消掉。  

釐清概念後就很簡單了。答案從0開始，如果nums2為奇數，則把nums1所有數字XOR進去；如果nums1為奇數，則把nums2所有數字XOR進去。  

時間複雜度O(M+N)，空間複雜度O(1)。  

```python
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        M=len(nums1)
        N=len(nums2)
        ans=0
        
        if M&1:
            for n in nums2:
                ans^=n
                
        if N&1:
            for n in nums1:
                ans^=n

        return ans
```
