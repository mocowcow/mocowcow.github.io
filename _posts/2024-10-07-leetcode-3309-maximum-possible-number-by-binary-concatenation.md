---
layout      : single
title       : LeetCode 3309. Maximum Possible Number by Binary Concatenation
tags        : LeetCode Medium Simulation Sorting Greedy
---
weekly contest 418。  
這題用 python 寫起來是真方便。  

## 題目

輸入大小為 3 的整數陣列 nums。  

你可以把 nums 任意排列，並將他們的**二進制表示**全部**連接**起來，求可得到的**最大**數值。  

注意：任何數的二進制表示都**不含**前導零。  

## 解法

首先將每個數轉成二進制字串。  

因為只有 3 個數，共只有 3! = 6 種排列。  
暴力枚舉所有排列，找到最大值即可。  

時間複雜度 O(log MX)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a = [bin(x)[2:] for x in nums]
        ans = 0
        for p in permutations(a):
            s = "".join(p)
            ans = max(ans, int(s, 2))

        return ans
```

如果改成 N 個數呢？總感覺可以按到某種規則排序，並找到最佳方案。  

根據直覺，二進制表示中，越多 1 靠左的數應該要擺在左邊。例如：  
> a = "11", b = "10"  
> ab = "1110", ba = "1011"  
> ab 確實大於 ba  

乍看之下以為是**字典序**較大者放左邊，然而並不是。反例：  
> a = "1", b = "10"  
> ab = "110", ba = "101"  
> 很明顯 ab 數值比 ba 更大，字典序是錯誤方法  

---

究竟怎麼判斷誰先呢？老朋友**鄰項交換法**又出場了。  
使用自定義排序，直接把兩種先後順序的數值算出來，看誰比較大就選誰。  
相似題 [179. Largest Number](https://leetcode.com/problems/largest-number/)。  

時間複雜度 O(log MX \* N \* log N)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:

        def cmp(a, b):
            ab = int(a + b, 2)
            ba = int(b + a, 2)
            # if ab > ba: # a first
            #     return -1
            # else: # b first
            #     return 1
            return ba - ab

        a = [bin(x)[2:] for x in nums]
        a.sort(key=cmp_to_key(cmp))

        return int("".join(a), 2)  
```
