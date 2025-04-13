---
layout      : single
title       : LeetCode 3513. Number of Unique XOR Triplets I
tags        : LeetCode Medium Math BitManipulation
---
biweekly contest 154。  
有點 codeforces 味道的構造題。  

## 題目

<https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/>

## 解法

從 [1..N] 中任選三個元素做 XOR，可重複選。  
求有能夠湊出幾種不同的結果。  

範例很好心告訴我們 N = 2 時，不管怎樣只能湊出 1,2。  
不難發現 N = 1 也只能湊出 1。  

---

但 N = 3 時竟然可以湊出 4 種，是哪 4 種？  
> 0,1,2,3

1^2^3 = 0，所以可以湊出一個 0。  
同理，對於 N >= 3 永遠可以湊出 0。  

---

那 N = 4 能不能變出新花樣？  
4 的二進位是 "1000"，有沒有把某些 0 變成 1，得到更大的數？  
只要找到 x^y 滿足後三個位不為 0，就可以和 4 組成大於 4 的數。  

因為 nums 有 [1..N] 的所有數字，既然有 4，那肯定有更小的數字。  
想要湊出 "111" 也很簡單，隨便找找 x = "110", y = "001" 就可以了。  
例如：  
> "1000" ^ "0110" ^ "0001"  
> = 8 ^ 6 ^ 1  
> = 15  

想弄出 "1110" 或 "1100" 當然也沒問題。反正只要某個位有出現過 1，就能透過某些組成把它搞成 1。  

所以最大值是依賴於 N 的**最高位**。  
若最高位是 m，則可得最大的值是 (1 << m) - 1。  
再加上 0 ，總共有 1 << m 種不同結果。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return N

        return 1 << N.bit_length()
```
