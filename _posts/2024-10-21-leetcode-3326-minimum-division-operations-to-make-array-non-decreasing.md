---
layout      : single
title       : LeetCode 3326. Minimum Division Operations to Make Array Non Decreasing
tags        : LeetCode Medium Math Greedy
---
weekly contest 420。  
這題時間限制很是奇妙，本來覺得不可能過的寫法卻過了。  

## 題目

輸入整數陣列 nums。  

正整數 x 的任何小於 x 的**正**因子都稱為 x 的**真因子**。  
例如 2 是 4 的真因子，但 6 不是 6 的真因子。  

你可以對 nums 執行任意次**操作**。每次選擇 nums 中的任意元素，並將其除以他的**最大真因子**。  

求使得陣列滿足**非遞減**的**最少操作次數**。若不可能則回傳 -1。  

## 解法

**最大真因子**簡稱 GPF。  
除了**質數**或是 1 以外，每個 x 都存在 GPF。  

操作即 x / GPF = q。  
因此只需要從 2 開始枚舉 x 的因子，找到第一個能整除 x 的因子就是操作結果，也就是**最小真因子** LPF。  

---

至於該從哪邊先開始操作？  
目標是使 nums 非遞減，而操作又只能把元素變小，nums 的最後一個數無論如何都不需要操作。  
而其餘的 nums[i] 必須要比 nums[i+1] 小，因此倒序遍歷，不合法時才操作；若不合法又找不到 LPF，則回傳 -1。  

---

雖然說做法已經出來了，但是還有幾個不太清楚的地方。  

問題一：對於同個 nums[i] 至多操作幾次？  
由於 LPF 是從小開始枚舉因子並回傳第一個，故保證是**質數**，所以**至多一次**。  
反證法：  

- 設 LPF(x) 為 q。  
- 若 q 不為質數，則 q 存在更小的真因子 p，且 p 也可整除 x。兩者矛盾。  

問題二：操作的複雜度是多少？  
由於是從小到大枚舉 q，而且因子是倆倆成對，至多只需枚舉到 sqrt(x)。  
因此 LPF 操作複雜度是 O(sqrt(x))。  

時間複雜度 O(N sqrt(MX))，其中 MX = max(nums)。  
空間複雜度 O(1)。  

雖然最壞情況下 O(N sqrt(MX)) 將近 1e8 計算量，但確實能通過，真的很神秘。  

```python
def lpf(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return i
    return -1

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        pre = inf
        for x in reversed(nums):
            # apply ops
            if x > pre:
                x = lpf(x)
                ans += 1
                # impossible
                if x > pre or x == -1:
                    return -1
            pre = x

        return ans
```

注意到 LPF(x) 是固定的，因此可以先預處理所有數的 LPF，之後都可以 O(1) 查詢。  
而且 LPF(x) 是**最小的質因子**，實際上跟**歐拉篩**的邏輯差不多。  
歐拉篩是以質數 q **標記其倍數**，只要改成將未標記的倍數 x 的 LPF 為 q 即可。  
預處理時間複雜度 O(MX log log MX)。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
MX = 10 ** 6
lpf = [-1] * (MX + 1)
for p in range(2, MX + 1):
    if lpf[p] == -1: # p is prime
        for x in range(p * p, MX + 1, p):
            if lpf[x] == -1: # no LPF yet
                lpf[x] = p

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        pre = inf
        for x in reversed(nums):
            # apply ops
            if x > pre:
                x = lpf[x]
                ans += 1
                # impossible
                if x > pre or x == -1:
                    return -1
            pre = x

        return ans
```
