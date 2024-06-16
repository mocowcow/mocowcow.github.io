---
layout      : single
title       : LeetCode 3186. Maximum Total Damage With Spell Casting
tags        : LeetCode Medium Array DP HashTable Sorting
---
周賽 402。相似題 [740. delete and earn]({% post_url 2022-02-07-leetcode-740-delete-and-earn %})。  
根據原題搞了奇怪的寫法，浪費不少時間。  

## 題目

一個魔術師有好幾個法術。  

輸入整數陣列 power，代表每個法術的傷害。不同的法術可以擁有相同的傷害。  

已知若法師使用傷害為 power[i] 的法術，則之後無法使用傷害為 power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2  的其他任意法術。  

每個法術只能使用一次。  
求法師可造成的**最大總傷害值**。  

## 解法

假設有數個法術傷害都是 x，那麼當然要全部都用。  
先用雜湊表統計各傷害的出現次數。  

原本做法是考慮每個傷害值為 i 的法術選或不選。若選，之後只能從 i - 3 繼續；若不選，則從 i - 1 繼續。  
定義 dp(i)：使用從傷害值 0 到 i 的所有法術，可造成的最大傷害。  
轉移：dp(i) = max(dp(i - 1), dp(i - 3) + cnt[i] * i)  
base：當 i <= 0，沒有剩餘法術，回傳 0。  

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        N = len(power)
        d = Counter(power)
        
        @cache
        def dp(i):
            if i <= 0:
                return 0
            return max(
                dp(i - 1),
                dp(i - 3) + d[i] * i
            )
        
        return dp(max(d))
```

但是 power[i] 的範圍高達 10^9，逐一枚舉肯定會超時，需要其他方法優化。  
我們改成只枚舉**有出現**的傷害值 x，並從前一個傷害進行轉移。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        N = len(power)
        d = Counter(power)
        keys = sorted(d)
        
        @cache
        def dp(i):
            if i < 0:
                return 0
            x = keys[i]
            j = bisect_right(keys, x - 3) - 1
            return max(
                dp(i - 1),
                dp(j) + d[x] * x
            )
        
        return dp(len(d) - 1)
```
