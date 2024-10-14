---
layout      : single
title       : LeetCode 3316. Find Maximum Removals From Source String
tags        : LeetCode Medium DP
---
biweekly contest 141。  
這題又是很妙的測資範圍，還要猜會不會過。  

## 題目

輸入長度 n 的字串 source，和另一個字串 pattern，且保證 pattern 是 source 的子序列。  
還有一個**有序的**整數陣列 targetIndices，由 [0, n - 1] 中的**不同**數字組成。  

定義一次**操作**為刪除位於索引 source[idx] 的字元，且滿足：  

- idx 是 targetIndices 中的元素。  
- 在刪除該字元後， pattern 依然是 source 的子序列。  

刪除操作並不會改變字串中的索引位置。例如從 "abc" 中刪除 'c' 之後，索引 2 的字元依然是 'b'。  

求**最多**可以操作幾次。  

## 解法

相似題 [1143. longest common subsequence]({% post_url 2022-02-08-leetcode-1143-longest-common-subsequence %})。  
子序列問題會直接想到 dp，枚舉字元選或不選。  

差別在於本題多出了**刪除操作**，並要求操作盡可能多次。  

---

定義 dp(i, j)：在 source[i..] 中匹配子序列 pattern[j..] 的最大刪除次數。  
轉移：dp(i, j) = max(選, 不選, 刪除)。  

- 若 source[i] = pattern[j] 可選，dp(i+1, j+1)。  
- 不選則跳過當前字元，dp(i+1, j)。  
- 若 i 位於 targetIndices 之中可刪除，dp(i+1, j) + 1。  

base：當 i = M 且 j = M 時匹配成功，且無法繼續刪除，回傳 0；若只有 i = M 則匹配失敗，回傳 -inf 代表不合法。  

答案入口為 dp(0, 0)。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        M, N = len(source), len(pattern)
        s = set(targetIndices)

        @cache
        def dp(i, j):
            if i == M and j == N:
                return 0
            if i == M:
                return -inf

            # no take
            res = dp(i+1, j)

            # take
            if j < N and source[i] == pattern[j]:
                res = max(res, dp(i+1, j+1))

            # op
            if i in s:
                res = max(res, dp(i+1, j) + 1)
            return res

        ans = dp(0, 0)
        dp.cache_clear()

        return ans
```

注意到**刪除**和**跳過不選**兩種方式都是基於 dp(i+1, j) 的，差別在於刪除需要多加 1。  
可以把兩者合併成同一項。  

順便改成遞推寫法。  

```python
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        M, N = len(source), len(pattern)
        s = set(targetIndices)

        f = [[-inf] * (N+1) for _ in range(M+1)]
        f[M][N] = 0

        for i in reversed(range(M)):
            for j in reversed(range(N + 1)):
                res = f[i+1][j] + int(i in s) # no take / op
                if j < N and source[i] == pattern[j]: # take
                    res = max(res, f[i+1][j+1])
                f[i][j] = res

        return f[0][0]
```
