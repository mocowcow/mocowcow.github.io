---
layout      : single
title       : LeetCode 3144. Minimum Substring Partition of Equal Character Frequency
tags        : LeetCode Medium Array String DP HashTable
---
雙周賽 130。聽說這題又在卡常數，很多人莫名超時，看來是我運氣好沒中獎。  

## 題目

**平衡的**字串指的是其包含的所有字元出現次數都相同。  

輸入字串 s，你必須將其分割成一或多個**平衡的**子字串。  
例如 s == "ababcc"，則 ("abab", "c", "c"), ("ab", "abc", "c") 和 ("ababcc") 都是合法的分割方式。  
但 ("a", "bab", "cc"), ("aba", "bc", "c") 和 ("ab", "abcc") 不合法。  

求合法分割的**最少**子字串個數。  

## 解法

經典的劃分型 dp，枚舉分割點並更新答案最小值。  

定義 dp(i)：子字串 s[i..N-1] 的合法最小子字串個數。  
轉移：dp(i) = min(dp(j + 1) + 1) FOR ALL 平衡的 s[i..j]  
base：當 i = N，分割完畢，回傳 0。  

枚舉分割點 j 時需要判斷是否**平衡**，確定平衡才進行轉移。  
統計出現頻率用雜湊表或是陣列都行，檢查頻率想用集合或是檢查最大最小也都可以。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        N = len(s)
        
        @cache
        def dp(i):
            if i == N:
                return 0
            d = Counter()
            res = inf
            for j in range(i, N):
                d[s[j]] += 1
                # if len(set(d.values())) == 1: # only 1 freq
                for v in d.values():
                    if v != d[s[j]]:
                        break
                else:
                    res = min(res, dp(j + 1) + 1)
            return res
        
        return dp(0)
```

改成遞推版本。  
順便加上小小的剪枝：s[i..j] 大小必為已出現字元的倍數，否則不可能是平衡的。  

```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        for i in reversed(range(N)):
            d = Counter()
            res = inf
            for j in range(i, N):
                d[s[j]] += 1
                if (j - i + 1) % len(d) != 0: # cannot be balanced
                    continue
                for v in d.values():
                    if v != d[s[j]]:
                        break
                else:
                    res = min(res, dp[j + 1] + 1)
            dp[i] = res
        
        return dp[0]
```
