---
layout      : single
title       : LeetCode 3186. Maximum Total Damage With Spell Casting
tags        : LeetCode Medium Array DP HashTable Sorting TwoPointers BinarySearch
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

先將有出現的**有出現**的傷害值排序，記做 keys。  
我們改成枚舉第 i 個 key，並從最後一個滿足 keys[j] + 2 < keys[i] 的第 j 個傷害值轉移。  

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
            j = bisect_left(keys, x - 2) - 1
            return max(
                dp(i - 1),
                dp(j) + d[x] * x
            )
        
        return dp(len(d) - 1)
```

若使用傷害值 x 的法術，必須從 x - 3 轉移而來。  
就算暴力從 keys[i] 往回找，最多也只會找三次。可以把二分換成暴力迴圈。  

時間複雜度 O(N)。  
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
            j = i - 1
            while j >= 0 and x - keys[j] <= 2:
                j -= 1
            return max(
                dp(i - 1),
                dp(j) + d[x] * x
            )
        
        return dp(len(d) - 1)
```

轉成遞推寫法。  
為了處理 dp(-1) 的狀態，對於每個狀態都加上偏移量 1。  

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        N = len(power)
        d = Counter(power)
        keys = sorted(d)
        M = len(keys)

        dp = [0] * (M + 1)
        for i, x in enumerate(keys):
            j = i 
            while j >= 0 and x - keys[j] <= 2:
                j -= 1
            dp[i + 1] = max(
                dp[i],
                dp[j + 1] + d[x] * x
            )
            
        return dp[M]
```

如果今天法術之間的間隔不只是 2 而是 k，那暴力迴圈就不行，只能用二分的方式。  
但注意到這個 j 只會隨著 i 一起增加，其實可以用雙指針維護 j 的位置，不斷遞增到 keys[i] 和 key[j] 差距為 k 為止。  

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        N = len(power)
        d = Counter(power)
        keys = sorted(d)
        M = len(keys)

        dp = [0] * (M + 1)
        best_j = 0
        j = 0
        for i, x in enumerate(keys):
            while x - keys[j] > 2:
                best_j = max(best_j, dp[j + 1])
                j += 1
            dp[i + 1] = max(
                dp[i],
                best_j + d[x] * x
            )
            
        return dp[M]
```

最後說說的的奇怪寫法，雖然浪費不少時間才搞出來，但是空間複雜度比上述幾個方法都更低。  

先回到最上面枚舉傷害值 i 的最原始版本。  
轉移方程式：dp(i) = max(dp(i - 1), dp(i - 3) + cnt[i] * i)  
會發現實際上只需要保留前三個狀態 dp(i - 1), dp(i - 2), dp(i - 3)。  

分別設 dp0, dp1, dp2 代表 dp(i - 1), dp(i - 2), dp(i - 3)。  
每次轉移時：  

- dp2' = max(dp2, dp0 + cnt[i] * i)  
- dp1' = dp2  
- dp0' = dp1  

---

改成枚舉有出現的傷害 x 之後，要如何從上一個傷害 prev 轉移過來？  
照著原本做法應該要轉移 prev - x 次。而且因為法術沒有出現，只會改變 dp0, dp1 的值，dp2 維持不變。  
只需要轉移：  

- dp1' = dp2  
- dp0' = dp1  

觀察上面規律發現，**轉移 3 次後**就會使得 dp2 = dp1 = dp0，第四次開始就不會改變值，沒有必要繼續轉移。  
因此除了套用 x 的**最後一次**轉移以外，先前至多只需要轉移 2 次。  

舉個例子：  
> keys = [1, 99]  
> 當前 x = 1  
> dp0, dp1, dp2 = 0, 0, 1  
> 當前 x = 2  
> dp0, dp1, dp2 = 0, 1, 1  
> 當前 x = 3  
> dp0, dp1, dp2 = 1, 1, 1  
> ...
> 當前 x = 99  
> dp0, dp1, dp2 = 1, 1, 100  
> 當前 x = 100  
> dp0, dp1, dp2 = 1, 100, 100  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        N = len(power)
        d = Counter(power)
        keys = sorted(d)

        dp0 = dp1 = dp2 = 0
        prev = -inf
        for x in keys:
            for _ in range(min(2, x - prev - 1)):
                dp0, dp1 = dp1, dp2
            dp0, dp1, dp2 = dp1, dp2, max(dp2, dp0 + d[x] * x)
            prev = x
            
        return dp2
```
