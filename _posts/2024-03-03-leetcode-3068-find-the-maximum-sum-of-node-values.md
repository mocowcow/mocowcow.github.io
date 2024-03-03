---
layout      : single
title       : LeetCode 3068. Find the Maximum Sum of Node Values
tags        : LeetCode Hard Array Graph DP
---
雙周賽125。

## 題目

有一個**無根**的樹，共有 n 個節點，編號分別從 0 到 n-1。  
輸入二維整數陣列 edges，其中 edges[i] = [u<sub>i</sub>, b<sub>i</sub>]，代表 a<sub>i</sub> 和 b<sub>i</sub> 之間存在一條邊。  
另外還有整數 k ，以及長度同為 n 的陣列 nums，其中 nums[i] 代表第 i 個節點的值。  

你可以執行以下操作任意次：  

- 選擇任意邊 [u, v]，更新兩節點的值：  
  - nums[u] = nums[u] XOR k
  - nums[v] = nums[v] XOR k

求任意次操作後，將所有節點的值加總，**最多**能夠得到多少。  

## 解法

先回顧 XOR 的特性：倆倆相消。如果一個值對 k 做 XOR 兩次，等於沒做。  
因此每個節點只有做或不做兩個狀態。  

操作是選擇邊，所以每次都會有兩個節點受到影響。最後有做 XOR 的節點個數一定是偶數。  
難點在於：怎麼決定選些點來做 XOR？  

---

仔細想想，如果有 [a, b, c, d] 四個點直線相連，要選擇 a, b 兩個肯定是可以的。  
那如果是 a, c 呢？可以先操作 [a, b]，然後再操作 [b, c] 這樣就得到 a, c 了。  
發現有幾多少邊根本不重要，只要有相連，就可以透過某些操作來**選擇任意偶數個節點**。  
而題目說了是樹，代表每個節點都是連通的。  

---

但是沒有一個很明顯的方案去判斷節點選不選，因此考慮 dp。  
以選擇個數的**奇偶**作為狀態。  

定義 dp(i, parity)：代表 nums[i:N] 中，選擇奇/偶數個值做 XOR 的最大總和。其中 parity = 0 代表偶數個。  
轉移：  

- dp(i, even) = max(nums[i] + prev_even, (nums[i] ^ k) + prev_odd)  
- dp(i, odd) = max(nums[i] + prev_odd, (nums[i] ^ k) + prev_even)  

BASE：當 i=N，代表沒有節點了。如果還需要奇數個則不合法，回傳 -inf；否則合法，回傳 0。  

因為只能選偶數個，所以答案入口是 dp(0, 0)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        
        @cache
        def dp(i, parity):
            if i == N and parity == 1: # odd count is invalid
                return -inf
            if i == N:
                return 0
            
            prev_even = dp(i + 1, 0)
            prev_odd = dp(i + 1, 1)
            if parity == 0: # even
                return max(nums[i] + prev_even, (nums[i] ^ k) + prev_odd)
            else: # odd
                return max(nums[i] + prev_odd, (nums[i] ^ k) + prev_even)
        
        return dp(0, 0) # must be even
```

改成遞推版本。  

```python
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        dp = [[0, 0] for _ in range(N + 1)]
        dp[-1][1] = -inf
        
        for i in reversed(range(N)):
            prev_even = dp[i+1][0]
            prev_odd = dp[i+1][1]
            dp[i][0] = max(nums[i] + prev_even, (nums[i] ^ k) + prev_odd)
            dp[i][1] = max(nums[i] + prev_odd, (nums[i] ^ k) + prev_even)
        
        return dp[0][0]

        
```

發現對於 dp(i) 來說只需要參考上一個狀態，空間可以壓縮掉。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        even, odd = 0, -inf
        for x in nums:
            even, odd = max(even + x, odd + (x ^ k)), max(even + (x ^ k), odd + x)
            
        return even
```
