---
layout      : single
title       : LeetCode 3428. Maximum and Minimum Sums of at Most Size K Subsequences
tags        : LeetCode Medium Math Sorting
---
weekly contest 433。  
這題也不太簡單，至少比 Q3 還難，建議換個順序。  

## 題目

<https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/>

## 解法

光是枚舉所有**子序列**就要 O(2^N)，肯定超時。  

可以改枚舉所有元素 x，看 x 在幾個子序列中做為極值。  
若 x 在 cnt 個子序列中做為最大值，則對答案的貢獻是 x \* cnt；  
同理，若 x 在 cnt 個子序列中做為最小值，則對答案的貢獻是 x \* cnt。  

---

那如何知道 x 在哪些子序列中扮演最大值？  
只要小於等於 x 的元素，無論選幾個，都不會改變 x 做為最大值的事實。  

為了方便知道有多少個小於等於 x 的元素，先將 nums 排序。  
枚舉 nums[i] = x 時，就有 i 個小於等於 x 的元素可選或不選。  

並且受到子序列大小至多為 k 的限制，除了 x 以外，至多可以從 i 個元素中再選 k-1 個。  
故 x 做為最大值的貢獻次數為 sum(comb(i, j) FOR 0 <= j <= k-1)。  

---

組合數可以用遞推預處理，最壞情況下需要從 N = 10^5 個元素中選 K = 100 個元素。  
預處理時間複雜度 O(NK)。  

先遞增排序，枚舉 x 做為最大值求貢獻。  
然後遞減排序，枚舉 x 做為最小值求貢獻。  
兩貢獻相加即為答案。  

時間複雜度 O(N log N + NK)。  
空間複雜度 O(1)。  

```python
MX = 10**5+5
MXK = 100+5
MOD = 10**9+7
C = [[0]*(MXK+1) for _ in range(MX+1)]
C[0][0] = 1
for i in range(1, MX+1):
    C[i][0] = 1
    for j in range(1, MXK+1):
        C[i][j] = (C[i-1][j-1]+C[i-1][j]) % MOD


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        # x 做為最大值貢獻
        ans = 0
        nums.sort()
        for i, x in enumerate(nums):
            for j in range(k):
                ans += C[i][j] * x
                ans %= MOD

        # x 做為最小值的貢獻
        nums.reverse()
        for i, x in enumerate(nums):
            for j in range(k):
                ans += C[i][j] * x
                ans %= MOD

        return ans
```

其實也不必拆成兩部分。  
因為在 nums 有序遞增時，對於 nums[i] = x 來說有 i 個小於等於 x 的元素；  
基於**對稱性**，也有 N-1-i 個大於等於 x 的元素。  

兩者可以合併在一次迴圈計算。  

```python
nums.sort()
for i, x in enumerate(nums):
    for j in range(k):
        # x 做為最大值貢獻
        ans += C[i][j] * x
        # x 做為最小值貢獻
        ans += C[N-1-i][j] * x
        ans %= MOD
```

比賽時我把組合數陣列大小 NK 寫成 N^2 直接爆 MLE。  
沒注意到是寫錯，以為又被卡空間，直接換了一種做法。  

---

組合數除了巴斯卡三角形遞推以外，還可以用**階乘**來算。  
> comb(n, k) = f(n) / f(k) / f(n-k)  

但取餘數後，除法無法正確計算，因此需引入**乘法逆元**。  
同樣先預處理所有階乘以及階乘逆元，其餘部分同上。  

```python

```
