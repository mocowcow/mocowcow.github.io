---
layout      : single
title       : LeetCode 3472. Longest Palindromic Subsequence After at Most K Operations
tags        : LeetCode Medium
---
weekly contest 439。

## 題目

<https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/description/>

## 解法

k = 0 時，不能做任何修改，相當於 [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)。  
s[i..j] 能得到的最長回文子序列，肯定是由更小的子問題 s[i+1..j-1]、s[i+1..j] 或 s[i..j-1] 組成。  

---

考慮透過修改使 s[i] 變成 s[j]。  
相似題 [3106. lexicographically smallest string after operations with constraint]({% post_url 2024-04-07-leetcode-3106-lexicographically-smallest-string-after-operations-with-constraint %})。  

令 s[i], s[j] = x, y。  
我們不知道 x, y 的相對大小，只能用 abs(x - y) 求兩者的差。  
但 x, y = 'a', 'z' 時，向左邊修改明顯更好。整個循環長度是 26，所以向左改的次數就是 26 - abs(x - y)，兩者需取最小值。  

也可以從另一種角度思考：反正是循環的，相減得到負數也沒關係，最後 MOD 26 就會得到正確的值。  
至少需要操作 min((x - y) % 26, (y - x) % 26)。  

---

在 516 題的基礎上，多加一個狀態 rem。  
定義 dp(i, j, rem)：子字串 s[i..j] 修改至多 rem 次可得到的最長回文子序列。  
s[i], s[j] 所需修改次數 op 不超過 rem 時額外從 dp(i+1, j-1, rem-op) 轉移。  

時間複雜度 O(N^2 \* k)。  
空間複雜度 O(N^2 \* k)。  

```python
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        N = len(s)
        a = [ord(c) - 97 for c in s]

        @cache
        def dp(i, j, rem):
            if i == j:
                return 1
            if i > j:
                return 0

            x, y = a[i], a[j]
            if x == y:
                return dp(i + 1, j - 1, rem) + 2

            op = min((x - y) % 26, (y - x) % 26)
            res = max(dp(i + 1, j, rem), dp(i, j - 1, rem))
            if rem >= op:
                res = max(res, dp(i + 1, j - 1, rem - op) + 2)
            return res

        return dp(0, N - 1, k)
```
